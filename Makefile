PROJECT_NAME=p_app

USER_OR_VENV := --USER_OR_VENV
ifdef VIRTUAL_ENV
USER_OR_VENV :=
endif

all: install test document


install-requirements: clean
	pip install pytest
	pip install sphinx
	pip install sphinx-rtd-theme
	pip install -r requirements.txt

install: install-requirements reports-init
	python setup.py install

reports-init:
	mkdir -p reports

black:
	black $(PROJECT_NAME)

lint: reports-init black
	- pylint $(PROJECT_NAME) # -r n --msg-template="{msg_id}:{line:3d},{column}: {obj}: {msg} ({symbol})" > reports/pylint-report.txt

test:
	coverage run -m pytest -v
	coverage report --omit='test*'

document: install
	sphinx-build doc build/doc

clean:
	rm -rf build dist .pytest_cache *egg* .coverage app.log reports
