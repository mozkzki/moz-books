.PHONY: black flake8 ut start google opendb rakuten calil doc

all: lint ut

lint: flake8 black

black:
	black --line-length=100 ./src ./tests

flake8:
	flake8 --max-line-length=100 --ignore=E203,W503 ./src ./tests

ut:
	pytest -v --capture=no --cov-config .coveragerc --cov=src --cov-report=xml --cov-report=term-missing .

start:
	python ./examples/all.py

google:
	python ./examples/google.py

opendb:
	python ./examples/opendb.py

rakuten:
	python ./examples/rakuten.py

calil:
	python ./examples/calil.py

doc:
	./scripts/doc.sh && open docs/_build/index.html
