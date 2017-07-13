.PHONY: docs

TAG = $(shell node -pe 'require("./package.json").version')
PROJECT = $(shell node -pe 'require("./package.json").name')
SHELL = /bin/bash

default: help

define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:  ## Print this help
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean:  ## Cleanup the codebase from temp files
	@find . -name '*.pyc' | xargs rm -rf
	@find . -name '*.egg-info' | xargs rm -rf

requirements:  ## Install back-end requirements
	@pip install -e .
	@pip install -e .[deploy,dev]

backend: requirements  ## Build back-end
	python manage.py migrate

frontend:  ## Build front-end
	yarn install --ignore-engines

develop: clean frontend backend  ## Build front- and backend

test:  ## Run complete test suite, with new DB
	py.test tests/

qt:  ## Quickly run tests, with same DB
	py.test -q --reuse-db tests/newspaper

coverage:  ## Run tests and open coverage report
	@coverage run --source newspaper -m py.test -q --reuse-db --tb=short tests/newspaper
	@coverage report -m
	@coverage html
	@$(BROWSER) htmlcov/index.html

lint:  ## Check your code for style errors
	@isort --check-only --recursive src/
	@flake8 src/

sort:  ## Sort python imports automatically, be carefull!
	@isort --recursive src/

docs:  ## Generate and open documentation
	@make -C docs html
	@$(BROWSER) docs/build/html/index.html

makemessages:  ## Collect all gettext translatable strings
	cd src/newspaper && python ../../manage.py makemessages -a

compilemessages:  ## Compile all translated gettext strings
	cd src/newspaper && python ../../manage.py compilemessages

package:  ## Build installable Python package
	python setup.py sdist

docker-build: package  ## Build Docker container
	docker build -t $(PROJECT) .

local-docker-run: docker-build  ## Run docker container locally
	docker run --name $(PROJECT) -d -P -p 8000:80 -e DJANGO_CONFIGURATION=Development $(PROJECT)

local-docker-ssh:  ## SSH into local (running) docker container
	docker exec -it $(PROJECT) /bin/sh

local-docker-destroy:  ## Destroy and remove local docker container
	@docker kill $(PROJECT)
	@docker rm -f $(PROJECT)
	@docker rmi -f $(PROJECT)
