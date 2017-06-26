import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Mattermost API v4 Wrapper",
    version = "0.0.1",
    author = "Brian Hopkins",
    author_email = "btotharye@gmail.com",
    description = ("A mattermost api v4 wrapper to interact with api"),
    license = "MIT",
    keywords = "mattermost wrapper api",
    url = "https://btotharye.com",
    packages=find_packages(),
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
    ],
)
