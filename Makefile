docs:
	scripts/generate-docs
	rsync -rh --inplace \
		doc/* \
		Geils:~/www/burntsushi.net/public_html/doc/nflgame/

pypi: docs
	sudo python2 setup.py register sdist upload

pypi-meta:
	python2 setup.py register

pep8:
	pep8-python2 src/pywingo/{__init__,pywingo}.py

push:
	git push origin master
	git push github master
