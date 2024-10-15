"""Package test module."""

import re

import poetry_git_branch_plugin


def test_version():
    """Assert that `__version__` exists and is valid."""
    assert re.match(r"\d.\d.\d", poetry_git_branch_plugin.__version__)
