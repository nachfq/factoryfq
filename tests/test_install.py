import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='factory fq ')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.skills = self.base / 'skills'
        self.home = self.base / 'codex'
        self.target = self.skills / 'factoryfq'

    def run_installer(self, *args):
        return subprocess.run(
            [str(ROOT / 'install-codex.py'), '--skills-dir', str(self.skills), *args],
            env={**os.environ, 'CODEX_HOME': str(self.home)},
            text=True, capture_output=True, cwd=self.base,
        )

    def test_dry_run_creates_nothing(self):
        result = self.run_installer('--dry-run')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(list(self.base.iterdir()), [])

    def test_idempotent_skills_only_install_preserves_user_instructions(self):
        self.home.mkdir()
        for name in ('AGENTS.md', 'AGENTS.override.md', 'config.toml'):
            (self.home / name).write_text('User content\n')
        result = self.run_installer()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.target.resolve(), ROOT / 'skills')
        before = self.target.lstat().st_mtime_ns
        self.assertEqual(self.run_installer().returncode, 0)
        self.assertEqual(self.target.lstat().st_mtime_ns, before)
        for name in ('AGENTS.md', 'AGENTS.override.md', 'config.toml'):
            self.assertEqual((self.home / name).read_text(), 'User content\n')
        self.assertFalse((self.home / 'backups').exists())

    def test_install_does_not_create_codex_home_or_global_instructions(self):
        result = self.run_installer()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.home.exists())
        self.assertTrue((self.target / 'factory-project-plan/SKILL.md').is_file())
        self.assertFalse((self.target / 'omarchy-nvim-herdr').exists())

    def test_conflicting_file_requires_explicit_backup(self):
        self.skills.mkdir()
        self.target.write_text('Keep me\n')
        self.assertNotEqual(self.run_installer().returncode, 0)
        self.assertEqual(self.target.read_text(), 'Keep me\n')
        result = self.run_installer('--backup')
        self.assertEqual(result.returncode, 0, result.stderr)
        backup = next((self.home / 'backups/factoryfq').rglob('factoryfq'))
        self.assertEqual(backup.read_text(), 'Keep me\n')

    def test_real_directory_is_never_replaced(self):
        self.target.mkdir(parents=True)
        (self.target / 'custom').write_text('Keep me\n')
        self.assertNotEqual(self.run_installer('--backup').returncode, 0)
        self.assertEqual((self.target / 'custom').read_text(), 'Keep me\n')

    def test_broken_symlink_is_backed_up_and_unrelated_skills_untouched(self):
        self.skills.mkdir()
        other = self.skills / 'personal'
        other.mkdir()
        (other / 'SKILL.md').write_text('Personal\n')
        missing = self.base / 'missing'
        self.target.symlink_to(missing)
        self.assertNotEqual(self.run_installer().returncode, 0)
        self.assertEqual(self.run_installer('--backup').returncode, 0)
        backup = next((self.home / 'backups/factoryfq').rglob('factoryfq'))
        self.assertEqual(os.readlink(backup), str(missing))
        self.assertEqual((other / 'SKILL.md').read_text(), 'Personal\n')

    def test_failed_link_creation_restores_target(self):
        spec = importlib.util.spec_from_file_location('factory_install', ROOT / 'install-codex.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.skills.mkdir()
        self.target.write_text('Restore me\n')
        with patch.object(Path, 'symlink_to', side_effect=OSError('simulated failure')):
            with self.assertRaises(OSError):
                module.install_link(ROOT / 'skills', self.target, self.home / 'backups')
        self.assertEqual(self.target.read_text(), 'Restore me\n')


if __name__ == '__main__':
    unittest.main()
