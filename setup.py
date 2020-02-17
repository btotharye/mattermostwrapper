# Always prefer setuptools over distutils
from setuptools import setup



setup(
    name="mattermostwrapper",
    packages=['mattermostwrapper'],
    version="2.2",
    author="Brian Hopkins",
    author_email="btotharye@gmail.com",
    url='https://github.com/btotharye/mattermostwrapper.git',
    download_url='https://github.com/btotharye/mattermostwrapper/archive/2.2.tar.gz',
    description=("A mattermost api v4 wrapper to interact with api"),
    license="MIT",
    install_requires=[
          'requests',
      ],
    classifiers=[],
)

