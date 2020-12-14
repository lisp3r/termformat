from os import path, system
from sys import exit, executable
from setuptools import setup, Command
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

class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        system(f'{executable} setup.py sdist bdist_wheel --universal')

        self.status('Uploading the package to PyPI via Twine…')
        system('twine upload dist/*')

        self.status('Pushing git tags…')
        system('git tag v{0}'.format(about['__version__']))
        system('git push --tags')

        exit()



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
    url='',
    packages=['termformat', 'tests'],
    cmdclass={
        'upload': UploadCommand,
    },
)

