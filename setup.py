#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='geotext',
    version='0.3.0',
    description='Geotext extracts countriy and city mentions from text',
    long_description=readme + '\n\n' + history,
    author='Yaser Martinez Palenzuela',
    author_email='yaser.martinez@gmail.com',
    url='https://github.com/elyase/geotext',
    packages=[
        'geotext',
    ],
    package_dir={'geotext': 'geotext'},
    include_package_data=True,
    package_data={
        'geotext': ['geotext/data/*.txt'],
    },
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='geotext',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements)
