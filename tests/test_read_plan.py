import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / 'skills/factory-project-plan/scripts/read_plan.py'


class ReadPlanTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='plan reader ')
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / 'repo'
        self.repo.mkdir()
        subprocess.run(['git', 'init', '-q', str(self.repo)], check=True)
        self.plans = self.repo / '.agent-context/plans'

    def run_reader(self, *args, repo=None, cwd=None):
        command = [sys.executable, str(SCRIPT)]
        if cwd is None:
            command.extend(['--repo', str(repo or self.repo)])
        return subprocess.run(command + list(args), cwd=cwd, text=True, capture_output=True)

    def write_plan(self, initiative_id='first', body='# Private body\n', **overrides):
        metadata = dict(id=initiative_id, title='First initiative', status='ready', depends_on=[])
        metadata.update(overrides)
        directory = self.plans / initiative_id
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / 'plan.md'
        path.write_text('---\n' + json.dumps(metadata, indent=2) + '\n---\n' + body)
        return path

    def test_list_reads_metadata_without_decoding_body_or_log(self):
        path = self.write_plan(depends_on=['previous'], custom_field={'allowed': True})
        with path.open('ab') as stream:
            stream.write(b'\xff')
        (path.parent / 'log.md').write_bytes(b'LOG MUST NOT APPEAR\xff')
        result = self.run_reader('list')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('first | First initiative | ready | depends_on: previous', result.stdout)
        self.assertIn('.agent-context/plans/first/plan.md', result.stdout)
        self.assertNotIn('Private body', result.stdout)
        self.assertNotIn('LOG MUST NOT APPEAR', result.stdout)

    def test_show_reads_only_selected_plan(self):
        selected = self.write_plan()
        other = self.write_plan('other')
        other.write_bytes(b'INVALID OTHER PLAN\xff')
        (selected.parent / 'log.md').write_bytes(b'INVALID LOG\xff')
        result = self.run_reader('show', 'first')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, selected.read_text())

    def test_missing_storage_creates_nothing(self):
        before = set(self.repo.rglob('*'))
        result = self.run_reader('list')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, 'No plans found.\n')
        missing = self.run_reader('show', 'missing')
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn('Plan not found', missing.stderr)
        self.assertEqual(set(self.repo.rglob('*')), before)

    def test_malformed_header_reports_error_and_keeps_valid_rows(self):
        self.write_plan()
        bad = self.write_plan('bad')
        bad.write_text('---\nnot JSON\n---\n# Body\n')
        result = self.run_reader('list')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('first |', result.stdout)
        self.assertIn('Error in bad:', result.stderr)
        self.assertIn('Invalid JSON metadata', result.stderr)

    def test_invalid_metadata_is_rejected(self):
        cases = [
            {'id': 'different'}, {'title': ' '}, {'status': 'unknown'},
            {'status': []}, {'depends_on': 'other'}, {'depends_on': ['first']},
            {'depends_on': ['other', 'other']}, {'depends_on': ['../other']},
        ]
        for fields in cases:
            with self.subTest(fields=fields):
                self.write_plan(**fields)
                result = self.run_reader('show', 'first')
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, '')
                self.assertNotIn('Traceback', result.stderr)

    def test_missing_delimiter_and_oversized_header_are_rejected(self):
        path = self.write_plan()
        for content in ['# No header\n', '---\n{}\n', '---\n' + 'x' * 70000]:
            with self.subTest(size=len(content)):
                path.write_text(content)
                result = self.run_reader('list')
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn('Traceback', result.stderr)

    def test_traversal_and_invalid_ids_are_rejected(self):
        for initiative_id in ['../outside', '/tmp/outside', '.', 'UPPER', 'two--hyphens']:
            with self.subTest(initiative_id=initiative_id):
                result = self.run_reader('show', initiative_id)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('Invalid initiative id', result.stderr)

    def test_repo_subdirectory_and_default_cwd_resolve_root(self):
        self.write_plan()
        subdirectory = self.repo / 'src/nested'
        subdirectory.mkdir(parents=True)
        for kwargs in [{'repo': subdirectory}, {'cwd': subdirectory}]:
            with self.subTest(kwargs=kwargs):
                result = self.run_reader('list', **kwargs)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn('.agent-context/plans/first/plan.md', result.stdout)

    def test_symlinks_at_each_storage_level_are_rejected(self):
        for relative in ['.agent-context', '.agent-context/plans',
                         '.agent-context/plans/first', '.agent-context/plans/first/plan.md']:
            with self.subTest(relative=relative):
                path = self.write_plan()
                original = self.repo / relative
                moved = Path(self.temp.name) / 'outside'
                original.rename(moved)
                original.symlink_to(moved, target_is_directory=moved.is_dir())
                for command in [('list',), ('show', 'first')]:
                    result = self.run_reader(*command)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn('Refusing symlink', result.stderr)
                original.unlink()
                moved.rename(original)
                self.assertTrue(path.is_file())

    def test_non_git_repository_fails_cleanly(self):
        result = self.run_reader('list', repo=Path(self.temp.name))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Cannot resolve Git repository', result.stderr)
        self.assertNotIn('Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main()
