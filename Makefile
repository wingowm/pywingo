docs:
	scripts/generate-docs
	rsync -rh --inplace \
		doc/* \
		Geils:~/www/burntsushi.net/public_html/doc/pywingo/

pypi: docs
	python2 setup.py register sdist upload

pypi-meta:
	python2 setup.py register

pep8:
	pep8-python2 src/pywingo/{__init__,commands,events}.py

gen: bins
	bin/gen-events ~/go/src/github.com/BurntSushi/wingo/event/events.go \
		> src/pywingo/events.py
	bin/gen-command-stubs > src/pywingo/commands.py

bins:
	go build -o bin/gen-events scripts/gen-events.go
	go build -o bin/gen-command-stubs scripts/gen-command-stubs.go

push:
	git push origin master
	git push github master
