#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#pip install https://github.com/jfbercher/tst_inst/archive/master.zip 
#pip install git+https://github.com/jfbercher/tst_inst#egg=ytst --user


"""lfm v3.0 - (C) 2001-15, by Iñigo Serna <inigoserna@gmail.com>

'Last File Manager' is a powerful file manager for UNIX console.
It has a curses interface and it's written in Python version 3.4+.
Released under GNU Public License, read COPYING file for more details.
"""


from distutils.core import setup
from os.path import join
from sys import exit, prefix, version_info, argv

myprefix="~/zazou"

if 'bdist_wheel' in argv:
    raise RuntimeError("This setup.py does not support wheels")

if 'install' in argv:
    print("Install in args")


DOC_FILES = ['COPYING', 'README', 'NEWS', 'TODO']
CONFIG_FILES = ['etc/lfm-default.keys', 'etc/lfm-default.theme']
MAN_FILES = ['lfm.1']

classifiers = """\
Development Status :: 5 - Production/Stable
Environment :: Console :: Curses
Intended Audience :: End Users/Desktop
Intended Audience :: System Administrators
License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
Natural Language :: English
Operating System :: POSIX
Operating System :: Unix
Programming Language :: Python :: 3
Topic :: Desktop Environment :: File Managers
Topic :: System :: Filesystems
Topic :: System :: Shells
Topic :: System :: System Shells
Topic :: Utilities
"""

print(__doc__)

# check python version
ver = (version_info.major, version_info.minor)
if ver < (3, 4):
    print('ERROR: Python 3.4 or higher is required to run lfm.')
    exit(-1)


setup(name='tst',
      version='3.0',
      description=__doc__.split("\n")[2],
      long_description='\n'.join(__doc__.split("\n")[2:]).strip(),
      author='jfb',
      author_email='@gmail.com',
      url='https://',
      platforms='POSIX',
      keywords=['file manager shell cli'],
      classifiers=filter(None, classifiers.split("\n")),
      license='GPL3+',
      packages=['zozo'],
      scripts=['zozo/zaza'],
      data_files=[(join(myprefix, 'doc/zozo'), DOC_FILES)],
      # **addargs
)
