.PHONY: install
install:
	poetry install

.PHONY: clear-cache
clear-cache:
	poetry run pre-commit clean

.PHONY: runserver
runserver:
	poetry run python -m core.manage runserver

.PHONY: shell
shell:
	poetry run python -m core.manage shell

.PHONY: showmigrations
showmigrations:
	poetry run python -m core.manage showmigrations

.PHONY: makemigrations
makemigrations:
	poetry run python -m core.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY: superuser
superuser:
	poetry run python -m core.manage createsuperuser

.PHONY: setup
setup: install migrate
