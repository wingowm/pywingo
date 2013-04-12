from distutils.core import setup
import os

longdesc = \
'''A Python 2.x library that communicates, within an active X session, with
wingo via sockets. Pywingo allows for easy scripting similar to how a person
would use `wingo-cmd` in a shell script by calling `gribble`.'''

# NOTE: Is this necessary?
#try:
#    docfiles = map(lambda s: 'doc/%s' % s, list(os.walk('doc'))[0][2])
#except IndexError:
#    docfiles = []

setup(
    name='pywingo',
    author='Drew Liszewski',
    author_email='drew.liszewski@gmail.com',
    maintainer='Andrew Gallant',
    maintainer_email='andrew@burntsushi.net',
    version='0.0.2',
    license='WTFPL',
    description='Provide access to wingo via sockets',
    long_description=longdesc,
    url='https://github.com/BurntSushi/pywingo',
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
    package_dir={'pywingo': 'src/pywingo'},
)
