#!/usr/bin/env python3
import os
import subprocess
import tempfile
from pathlib import Path
import shutil
import click

import inspect
import os
from pathlib import Path
current_dir = Path(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

def test1():
    path = Path(tempfile.mktemp(suffix=''))
    path.mkdir(parents=True)

    remote_repo = _make_remote_repo()

    (path / 'gimera.yml').write_text(f"""
repos:
    - url: "file://{remote_repo}"
      branch: branch1
      path: roles/X
      patches: []
      type: submodule
    - url: "file://{remote_repo}"
      branch: branch1
      path: roles2/X
      patches: []
      type: integrated
    """.replace("    ", "    "))
    subprocess.check_call(['git', 'init'], cwd=path)
    subprocess.check_call(['git', 'checkout', '-b', 'main'], cwd=path)
    (path / 'main.txt').write_text("main repo")
    subprocess.check_call(['git', 'add', 'main.txt'], cwd=path)
    subprocess.check_call(['git', 'commit', '-am', 'on main'], cwd=path)
    subprocess.check_call(["python3", current_dir.parent / 'gimera.py', 'apply'], cwd=path)


def _make_remote_repo():
    path = Path(tempfile.mktemp(suffix=''))
    path.mkdir(parents=True)
    subprocess.check_call(['git', 'init'], cwd=path)
    (path / 'file1.txt').write_text("random repo on main")
    subprocess.check_call(['git', 'add', 'file1.txt'], cwd=path)
    subprocess.check_call(['git', 'commit', '-am', 'on main'], cwd=path)

    (path / 'file1.txt').write_text("random repo on branch1")
    subprocess.check_call(['git', 'checkout', '-b', 'branch1'], cwd=path)
    subprocess.check_call(['git', 'add', 'file1.txt'], cwd=path)
    subprocess.check_call(['git', 'commit', '-am', 'on branch1'], cwd=path)

    return path

if __name__ == '__main__':
    test1()