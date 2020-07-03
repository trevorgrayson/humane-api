DEPDIR:=venv
PYTHON:=python3
export PYTHONPATH=.:$(DEPDIR)

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

clean: 
	find . -name *.pyc -delete
	rm -rf $(DEPDIR)
gitstatus:
	$(PYTHON) devboard/git.py

devboard:
	$(PYTHON) -m devboard

stonks:
	@mkdir -p data/stonks/wallstreetbets
	$(PYTHON) -m stonks

podcats:
	$(PYTHON) feeds/podcasts.py

.PHONY: feeds devboard
