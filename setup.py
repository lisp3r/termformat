from os import path, system
from sys import exit, executable
from setuptools import setup
from shutil import rmtree


NAME = 'termformat'
DESCRIPTION = 'Format terminal output'
VERSION = '1.0.0'

here = path.abspath(path.dirname(__file__))

try:
    with open(path.join(here, 'README.md')) as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

with open('LICENSE') as f:
    license = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='lisp3r',
    author_email='lisp3r@github.com',
    url='github.com/lisp3r/termformat.git',
    packages=['termformat', 'tests']
)
