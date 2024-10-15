import os
from unittest.mock import MagicMock, patch

from cleo.events.console_events import COMMAND
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


def test_set_git_branch_env_var_skips_non_env_command():
    """Test that the method does nothing for non-EnvCommand."""
    plugin = PoetryGitBranchPlugin()
    event = MagicMock()
    dispatcher = MagicMock()

    # Reset the environment variable before the test.
    if "POETRY_GIT_BRANCH" in os.environ:
        del os.environ["POETRY_GIT_BRANCH"]

    event.command = MagicMock()  # Set it so it is not an EnvCommand
    plugin.set_git_branch_env_var(event, "command", dispatcher)

    assert os.environ.get("POETRY_GIT_BRANCH") is None


def test_activate():
    """Test that the activate method."""
    # Create a mock Application object
    mock_application = MagicMock()
    mock_event_dispatcher = MagicMock()
    mock_application.event_dispatcher = mock_event_dispatcher

    # Create an instance of the class that contains the 'activate' method
    plugin = PoetryGitBranchPlugin()

    # Call the activate method
    plugin.activate(mock_application)

    # Check if the add_listener method was called with correct arguments
    mock_event_dispatcher.add_listener.assert_called_once_with(
        COMMAND, plugin.set_git_branch_env_var
    )
