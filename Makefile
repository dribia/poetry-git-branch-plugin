.PHONY: all clean check format test lint bump-version test-unit

PROJECT ?= poetry_git_branch_plugin
TESTS ?= tests

all:
	make clean
	make lint || exit 1
	make test || exit 1

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov
	rm -f .coverage

check: format lint

format:
	poetry run ruff format $(PROJECT) tests
	poetry run ruff check --fix --unsafe-fixes $(PROJECT) $(TESTS)

lint:
	poetry run ruff format --check $(PROJECT) $(TESTS)
	poetry run ruff check $(PROJECT) $(TESTS)
	poetry run mypy $(PROJECT)

lock:
	poetry lock --no-update

test:
	poetry run pytest --cov --cov-report=html --cov-report=xml

test-unit:
	poetry run pytest --cov --cov-report=html --cov-report=xml -m "not integration"

test-integration:
	poetry run pytest -m "integration"

bump-version:
	@old_version=$$(poetry version -s); echo "Current version: $${old_version}"; \
		commit_message=$$(poetry version "$(COMMIT_VERSION)"); \
		new_version=$$(poetry version -s); \
		if [ "$${old_version}" = "$${new_version}" ]; then \
			echo "$${old_version} version update did not change the version number."; \
			exit 0; \
		else \
		  poetry install; \
		  git commit pyproject.toml -m ":arrow_up: $${commit_message}"; \
		  git tag -a "v$${new_version}" -m ":arrow_up: $${commit_message}"; \
		fi
