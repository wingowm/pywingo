from distutils.core import setup
from glob import glob
import os

longdesc = \
'''A Python 2.x library that communicates, within an active X session, with
wingo via sockets. Pywingo allows for easy scripting similar to how a person
would use `wingo-cmd` in a shell script by calling `gribble`.'''

try:
    exfiles = map(lambda s: 'examples/%s' % s, list(os.walk('examples'))[0][2])
except IndexError:
    exfiles = []

setup(
    name='pywingo',
    author='Drew Liszewski',
    author_email='drew.liszewski@gmail.com',
    maintainer='Andrew Gallant',
    maintainer_email='andrew@burntsushi.net',
    version='0.0.12',
    license='WTFPL',
    description='Provide access to wingo via sockets',
    long_description=longdesc,
    url='https://github.com/wingowm/pywingo',
    classifiers=[
        'License :: Public Domain',
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Topic :: Desktop Environment :: Window Managers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    platforms='Linux',
    packages=['pywingo'],
    data_files=[('share/doc/pywingo', ['README.md', 'COPYING']),
                ('share/doc/pywingo/doc', glob('doc/pywingo/*.html')),
                ('share/doc/pywingo/examples', exfiles),
               ],
)
