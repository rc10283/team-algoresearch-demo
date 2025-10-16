# tests/test_ci_sanity.py
from pathlib import Path

def test_python_works():
    assert 1 + 1 == 2

def test_repo_has_readme():
    assert Path("README.md").exists(), "Add a README.md at the project root."
