Introduction
============
A Python 2.x library that communicates, within an active X session, with
wingo via sockets. Pywingo allows for easy scripting similar to how a person
would use `wingo-cmd` in a shell script by calling `gribble`.

Installation
============
pywingo is in the Python Package Index (PyPI):
http://pypi.python.org/pypi/pywingo

You can install it with:

```bash
sudo pip-2.7 install pywingo
```

Example
=======
    #!/usr/bin/python2

    import pywingo

    x = pywingo.Wingo()
    x.gribble('GetWorkspace')

