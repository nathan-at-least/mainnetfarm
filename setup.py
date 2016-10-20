#! /usr/bin/env python

from setuptools import setup, find_packages

PACKAGE = 'mainnetfarm'

setup(
    name=PACKAGE,
    description="",
    # url=
    # license=
    version='0.1',
    author='Nathan Wilcox',
    author_email='nathan@z.cash',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            '{0} = {0}.main:main'.format(PACKAGE),
            ],
        },
    )
