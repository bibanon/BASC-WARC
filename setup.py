#!/usr/bin/env python
# coding: utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()


setup(
    name='BASC-Warc',
    version='0.0.1',
    description=('Create and manage WARC files. '
                 'Currently in planning / pre-alpha stage.'),
    long_description=long_description,
    author='Daniel Oaks',
    author_email='daniel@danieloaks.net',
    url='https://github.com/bibanon/BASC-Warc',
    packages=['basc_warc'],
    package_dir={
        'basc_warc': 'basc_warc',
    },
    keywords='warc archive archiving',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Archiving',
    ]
)
