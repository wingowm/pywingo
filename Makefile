all:
	@echo "Specify a target."

docs:
	pdoc --html --html-dir ./doc --overwrite ./pywingo

pypi: docs
	python2 setup.py register sdist upload

dev-install: docs
	[[ -n "$$VIRTUAL_ENV" ]] || exit
	rm -rf ./dist
	python2 setup.py sdist
	pip install -U dist/*.tar.gz

pep8:
	pep8-python2 src/pywingo/{__init__,commands,events}.py

push:
	git push origin master
	git push github master

gen: bins
	bin/gen-events ~/go/src/github.com/BurntSushi/wingo/event/events.go \
		> src/pywingo/events.py
	bin/gen-command-stubs > src/pywingo/commands.py

bins:
	go build -o bin/gen-events scripts/gen-events.go
	go build -o bin/gen-command-stubs scripts/gen-command-stubs.go
