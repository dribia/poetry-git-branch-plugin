# Poetry Git Branch Plugin
A simple poetry plugin that sets an environment variable containint the name of the current checked-out branch before executing any poetry command.

## Why
Our main use case is in situations where DBT needs access to the current git branch name to set the name of the target schema.

## Installation
Install as any other poetry plugin:
```bash
poetry self add poetry-git-branch
```

## Development
If you are developing this plugin, you can install it locally by building a wheels file and installing it with your system-wide pip.
