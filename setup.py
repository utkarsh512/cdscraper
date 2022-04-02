#!/usr/bin/python3

from setuptools import setup
import io
import os

# Package meta-data
NAME = 'cdscraper'
DESCRIPTION = 'Scraping Create Debate'
URL = 'https://github.com/utkarsh512/cdscraper/'
EMAIL = 'imutkarshpatel@gmail.com'
AUTHOR = 'Utkarsh Patel'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = None

# Packages required
REQUIRED = ['requests', 'bs4', 'tqdm']

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=['cdscraper'],
    entry_points={
        'console_scripts': [
            'cdscraper = cdscraper.cli:run_as_command',
        ],
    },
    install_requires=REQUIRED,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
