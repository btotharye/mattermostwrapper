# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="Mattermost-API",
    version="1.1.0",
    author="Brian Hopkins",
    author_email="btotharye@gmail.com",
    description=("A mattermost api v4 wrapper to interact with api"),
    long_description=long_description,
    license="MIT",
    packages=find_packages(),
    install_requires=['requests'],
)

