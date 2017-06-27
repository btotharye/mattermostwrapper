# Always prefer setuptools over distutils
from setuptools import setup



setup(
    name="mattermost-wrapper",
    packages=['wrapper'],
    version="0.3",
    author="Brian Hopkins",
    author_email="btotharye@gmail.com",
    url='https://github.com/btotharye/mattermost_wrapper.git',
    download_url='https://github.com/btotharye/mattermost_wrapper/archive/0.1.tar.gz',
    description=("A mattermost api v4 wrapper to interact with api"),
    license="MIT",
    classifiers=[],
)

