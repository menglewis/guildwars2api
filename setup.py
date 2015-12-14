#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'requests'
]

test_requirements = []

setup(
    name='guildwars2api',
    version='0.6.0',
    description='A Python API Wrapper for the Guild Wars 2 API',
    long_description=readme + '\n\n' + history,
    author='David Lewis',
    author_email='meng.lewis@gmail.com',
    url='https://github.com/menglewis/guildwars2api',
    packages=[
        'guildwars2api',
        'guildwars2api.v1',
        'guildwars2api.v2',
        'tests',
    ],
    package_dir={'guildwars2api':
                 'guildwars2api'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='guildwars2api',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)