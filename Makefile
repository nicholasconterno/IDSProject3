.PHONY: install lint test

install:
	pip install -r requirements.txt

lint:
	flake8 src

test:
	pytest

run:
	python main.py