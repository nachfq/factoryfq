#!/usr/bin/env python3
"""Read a repository's initiative plans without modifying its files."""

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys


ID_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
STATUSES = {"draft", "ready", "active", "blocked", "done", "cancelled"}
MAX_HEADER_BYTES = 64 * 1024


class PlanError(Exception):
    """A repository or plan cannot be read safely."""


def validate_id(value):
    if not isinstance(value, str) or not ID_PATTERN.fullmatch(value):
        raise PlanError(f"Invalid initiative id: {value!r}")


def repository_root(path):
    try:
        result = subprocess.run(
            ["git", "-C", str(path), "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=False,
        )
    except OSError as error:
        raise PlanError(f"Cannot run Git: {error}") from error
    if result.returncode:
        raise PlanError(f"Cannot resolve Git repository at {path}: {result.stderr.strip()}")
    return Path(result.stdout.strip())


def check_path(path, *, directory=False):
    if path.is_symlink():
        raise PlanError(f"Refusing symlink: {path}")
    if not path.exists():
        return False
    if directory and not path.is_dir():
        raise PlanError(f"Expected directory: {path}")
    if not directory and not path.is_file():
        raise PlanError(f"Expected regular file: {path}")
    return True


def plans_directory(root):
    context = root / ".agent-context"
    if not check_path(context, directory=True):
        return None
    plans = context / "plans"
    return plans if check_path(plans, directory=True) else None


def plan_path(plans, initiative_id):
    validate_id(initiative_id)
    directory = plans / initiative_id
    if not check_path(directory, directory=True):
        raise PlanError(f"Plan not found: {initiative_id}")
    path = directory / "plan.md"
    if not check_path(path):
        raise PlanError(f"Plan not found: {initiative_id} ({path})")
    return path


def read_header(stream, initiative_id):
    # Unbuffered binary reads avoid consuming or decoding Markdown body bytes.
    lines = []
    size = 0
    while True:
        line = stream.readline(MAX_HEADER_BYTES - size + 1)
        size += len(line)
        if size > MAX_HEADER_BYTES:
            raise PlanError(f"Metadata header exceeds {MAX_HEADER_BYTES} bytes")
        if not line:
            raise PlanError("Missing closing metadata delimiter (---)")
        delimiter = line.rstrip(b"\r\n") == b"---"
        if not lines and not delimiter:
            raise PlanError("Plan must start with a metadata delimiter (---)")
        lines.append(line)
        if len(lines) > 1 and delimiter:
            break
    try:
        metadata = json.loads(b"".join(lines[1:-1]).decode("utf-8"))
    except (UnicodeError, ValueError) as error:
        raise PlanError(f"Invalid JSON metadata: {error}") from error
    if not isinstance(metadata, dict):
        raise PlanError("Metadata must be a JSON object")
    validate_id(metadata.get("id"))
    if metadata["id"] != initiative_id:
        raise PlanError("Metadata id must match the initiative directory")
    title = metadata.get("title")
    if not isinstance(title, str) or not title.strip():
        raise PlanError("Metadata title must be a nonempty string")
    status = metadata.get("status")
    if not isinstance(status, str) or status not in STATUSES:
        raise PlanError(f"Invalid metadata status: {status!r}")
    dependencies = metadata.get("depends_on")
    if not isinstance(dependencies, list):
        raise PlanError("Metadata depends_on must be a list")
    seen = set()
    for dependency in dependencies:
        validate_id(dependency)
        if dependency == initiative_id or dependency in seen:
            raise PlanError("Dependencies must be distinct other initiative ids")
        seen.add(dependency)
    return metadata, b"".join(lines)


def list_plans(root, plans):
    if plans is None:
        print("No plans found.")
        return 0
    errors = False
    count = 0
    for directory in sorted(plans.iterdir()):
        try:
            if directory.is_symlink():
                raise PlanError(f"Refusing symlink: {directory}")
            if not directory.is_dir():
                continue
            path = plan_path(plans, directory.name)
            with path.open("rb", buffering=0) as stream:
                metadata, _ = read_header(stream, directory.name)
            title = " ".join(metadata["title"].split())
            dependencies = ", ".join(metadata["depends_on"]) or "none"
            print(f'{metadata["id"]} | {title} | {metadata["status"]} | '
                  f'depends_on: {dependencies} | {path.relative_to(root)}')
            count += 1
        except (PlanError, OSError) as error:
            print(f"Error in {directory.name}: {error}", file=sys.stderr)
            errors = True
    if count == 0 and not errors:
        print("No plans found.")
    return int(errors)


def show_plan(plans, initiative_id):
    validate_id(initiative_id)
    if plans is None:
        raise PlanError(f"Plan not found: {initiative_id}")
    path = plan_path(plans, initiative_id)
    with path.open("rb", buffering=0) as stream:
        _, header = read_header(stream, initiative_id)
        try:
            content = (header + stream.read()).decode("utf-8")
        except UnicodeError as error:
            raise PlanError(f"Plan is not valid UTF-8: {path}") from error
    sys.stdout.write(content)
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Repository root or subdirectory (default: cwd)")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="List initiative metadata")
    show = commands.add_parser("show", help="Print one complete plan")
    show.add_argument("initiative_id")
    args = parser.parse_args(argv)
    try:
        if args.command == "show":
            validate_id(args.initiative_id)
        root = repository_root(args.repo)
        plans = plans_directory(root)
        if args.command == "list":
            return list_plans(root, plans)
        return show_plan(plans, args.initiative_id)
    except (PlanError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
