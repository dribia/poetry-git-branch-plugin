# Contribute

<p style="text-align: center; padding-bottom: 1rem;">
    <a href="/poetry-git-branch-plugin">
        <img
            src="../img/logo_dribia_blau_cropped.png"
            alt="Dribia"
            style="display: block; margin-left: auto; margin-right: auto; width: 40%;"
        >
    </a>
</p>

<p style="text-align: center;">
    <em>Contributions to Dribia libraries are always welcome!</em>
</p>

## Mantainers
poetry-git-branch-plugin is officially maintained by **Dribia Code - <code@dribia.com>**.

## Issues
Questions, feature requests and bug reports are all welcome as [discussions or issues](https://github.com/dribia/poetry-git-branch-plugin/issues).

Please note which version of the library are you using whenever reporting a bug.
```shell
python -c "import poetry-git-branch-plugin; print(poetry-git-branch-plugin.__version__)"
```

It would be very useful too to know which OS and Python version are your running poetry-git-branch-plugin from.

## Contribute
In order to contribute, the first step is to clone yourself the code:
[repository](https://github.com/dribia/poetry-git-branch-plugin):
```shell
git clone https://github.com/dribia/poetry-git-branch-plugin.git
```

Poetry is the best way to interact with this project, to install it, follow the official [Poetry installation guide](https://python-poetry.org/docs/#installation).
With poetry installed, one can install the project dependencies with:
```shell
poetry install
```

Now you should be ready to start coding and prepare your [pull request](https://github.com/dribia/poetry-git-branch-plugin/pulls).

!!! Warning
    Please, make sure to run:

    1. The project unit tests
    ```shell
    make test-unit
    ```
    2. The linters (`ruff` and `mypy`):
    ```shell
    make lint
    ```
    3. Apply all code formatting:
    ```shell
    make format
    ```

    before submitting your pull request.

Happy coding! 🎉