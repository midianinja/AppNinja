#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='backend',
    version='1.0',
    url='https://github.com/midianinja/AppNinja',
    description='AppNinja',
    author='Frente Hacker',
    packages=find_packages(exclude=('tests', 'tests.*')),
)
