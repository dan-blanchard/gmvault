"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from __future__ import absolute_import
from setuptools import setup

#APP = ['./gmv/gmv_cmd.py']
APP = ['./gmv_runner.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True, 'includes':['argparse', 'logbook','imapclient','chardet','six'],}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
