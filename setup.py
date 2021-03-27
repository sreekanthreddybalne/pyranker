from setuptools import setup, find_packages
from setuptools.command.test import test

# -*- coding: utf-8 -*-
import io
import re

from setuptools import setup

with io.open("README.md") as f:
    long_description = f.read()

with io.open("pyranker/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name='pyranker',
    version=version,
    description='pyranker helps you to store a re-orderable list in a database.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sreekanth Reddy Balne",
    author_email='whitehathackersree@gmail.com',
    maintainer="whitehathackersree",
    maintainer_email="whitehathackersree@gmail.com",
    license="BSD",
    url='https://github.com/whitehathackersree/pyranker',
    packages=find_packages(exclude=['tests', 'tests.*']),
    platforms='any',
    python_requires='>=3.6',
    zip_safe=False,
    setup_requires=['setuptools_scm'],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)