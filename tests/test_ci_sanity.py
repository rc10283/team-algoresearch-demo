# tests/test_ci_sanity.py
from pathlib import Path


def test_python_works():
    # Basic sanity check so CI can run at all
    assert 1 + 1 == 2


def test_repo_has_readme():
    # Helps catch empty repos or wrong checkout path in CI
    assert Path("README.md").exists(), "Add a README.md at the project root."
