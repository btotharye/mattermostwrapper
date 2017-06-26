from setuptools import setup, find_packages

install_requires = [
    'requests>=2.11.1',
]

def long_description():
    with codecs.open('README.md', encoding='utf8') as f:
        return f.read()

setup(
    name="Mattermost-API",
    version="1.0.0",
    author="Brian Hopkins",
    author_email="btotharye@gmail.com",
    description=("A mattermost api v4 wrapper to interact with api"),
    long_description=long_description,
    license="MIT",
    install_requires=install_requires,
    packages=find_packages(),
)
