#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='lsp-search',
    version='0.0.2',
    author='fenrisu1fr',
    author_email='simth.rock@8iy3.onmicrosoft.com',
    url='https://github.com/Jormungendr/lsp_search',
    description=u'Open your lsp soul.',
    packages=['lsp_search'],
    install_requires=['bs4'],
    entry_points={
        'console_scripts': [
            'lsp_search=lsp_search:lsp_search',
        ]
    }
)