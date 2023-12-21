# Poetry Git Branch Plugin
A simple poetry plugin that sets an environment variable containint the name of the current checked-out branch before executing any poetry command.

## Why
Our main use case is in situations where DBT needs access to the current git branch name to set the name of the target schema.

## Installation
Install as any other poetry plugin:
```bash
poetry self add poetry-git-branch-plugin
```

## Development
If you are developing this plugin, you can install it locally by building a wheels file
```bash
poetry build
```
and installing it with your system-wide or pyenv-wide pip.
```bash
# not inside pycharm nor inside a poetry shell
pip install /path/to/poetry-git-branch-plugin/dist/poetry_git_branch_plugin-0.1.0-py3-none-any.whl
```
