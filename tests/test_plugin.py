import os
from unittest.mock import MagicMock, patch

from poetry.console.commands.env_command import EnvCommand

from poetry_git_branch_plugin.plugin import PoetryGitBranchPlugin


@patch("os.popen")
def test_set_git_branch_env_var(mock_popen):
    """Test that the POETRY_GIT_BRANCH environment variable is set correctly."""

    plugin = PoetryGitBranchPlugin()
    event = MagicMock()
    dispatcher = MagicMock()

    # Reset the environment variable before the test.
    if "POETRY_GIT_BRANCH" in os.environ:
        del os.environ["POETRY_GIT_BRANCH"]

    mock_popen.return_value.read.return_value = "test-branch\n"

    event.command = EnvCommand()
    plugin.set_git_branch_env_var(event, "command", dispatcher)

    assert os.environ.get("POETRY_GIT_BRANCH") == "test-branch"
