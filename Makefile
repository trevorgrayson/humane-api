export PYTHONPATH=.:venv
PYTHON:=python3

compile: venv
venv: requirements.txt
	$(PYTHON) -m pip install -t venv -r requirements.txt 
	touch venv

testinplace:
	@PYTHONPATH=. python3 -m pytest --tb=line tests/tkts/ | python bin/test-in-place.py

test:
	@PYTHONPATH=. python3 -m pytest --tb=line tests/tkts/

feeds: compile
	@$(PYTHON) -m feeds

.PHONY: feeds
