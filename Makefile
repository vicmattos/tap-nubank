PYTHON_CMD = python3
# PYTHON_VERSION = 3.10
PYTHON_VERSION = $(shell $(PYTHON) -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
VENV = .venv
VENV_EXECS=$(VENV)/bin
VIRTUALENV_EXEC = virtualenv.pyz

# make it work on windows
ifeq ($(OS), Windows_NT)
    VENV_EXECS=$(VENV)/Scripts
    PYTHON_CMD=python
endif


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
