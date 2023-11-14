PYTHON_CMD = python3
PYTHON_VERSION = 3.10
VENV = .venv
VENV_EXECS=$(VENV)/bin
VIRTUALENV_EXEC = virtualenv.pyz

# make it work on windows
ifeq ($(OS), Windows_NT)
    VENV_EXECS=$(VENV)/Scripts
    PYTHON_CMD=python
endif


.PHONY: setup
setup: $(VENV)
	$(VENV_EXECS)/pip install -r requirements-dev.txt
	$(VENV_EXECS)/pre-commit install-hooks
	$(VENV_EXECS)/pre-commit install
	$(VENV_EXECS)/pip install -e .


.PHONY: format
format: $(VENV)
	$(VENV_EXECS)/pre-commit run ruff-format --all-files


.PHONY: lint
lint: $(VENV)
	$(VENV_EXECS)/pre-commit run ruff --all-files
	$(VENV_EXECS)/pre-commit run mypy --all-files


.PHONY: test
test: $(VENV)
	$(VENV_EXECS)/tox -e dev


.PHONY: clean
clean:
	rm -rf \
		.mypy_cache \
		.ruff_cache \
		.tox \
		src/tap_nubank/__pycache__ \
		src/tap_nubank.egg-info \
		tests/__pycache__


$(VIRTUALENV_EXEC):
ifndef PYTHON_VERSION
	$(error Please set PYTHON_VERSION variable in Makefile)
endif
	curl https://bootstrap.pypa.io/virtualenv/$(PYVERSION)/virtualenv.pyz --output $(VIRTUALENV_EXEC)

$(VENV): $(VIRTUALENV_EXEC)
	$(PYTHON_CMD) $(VIRTUALENV_EXEC) $(VENV)
	$(VENV_EXECS)/pip install --upgrade pip

requirements.txt: $(VENV) pyproject.toml
	$(VENV_EXECS)/pip-compile

requirements-dev.txt: $(VENV) pyproject.toml
	$(VENV_EXECS)/pip-compile --extra=dev --output-file=requirements-dev.txt

requirements-test.txt: $(VENV) pyproject.toml
	$(VENV_EXECS)/pip-compile --extra=test --output-file=requirements-test.txt
