#!/usr/bin/env python
import codecs
import os.path
import re

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


requires = [
        # TODO
]

setup(
    name='amazon-transcribe-streaming-sdk',
    version=find_version("amazon-transcribe-streaming", "__init__.py"),
    description='Async Python SDK for Amazon Transcribe Streaming',
    long_description=open('README.rst').read(),
    author='Amazon Web Services',
    url='https://github.com/awslabs/amazon-transcribe-streaming-sdk',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=requires,
    extras_require={},
    license="Apache License 2.0",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
