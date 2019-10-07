#!/usr/bin/env python
# -*- coding: utf-8 -*-

# For a fully annotated version of this file and what it does, see
# https://github.com/pypa/sampleproject/blob/master/setup.py

# To upload this file to PyPI you must build it then upload it:
# python setup.py sdist bdist_wheel  # build in 'dist' folder
# python-m twine upload dist/*  # 'twine' must be installed: 'pip install twine'


import ast
import io
import re
import os
from setuptools import find_packages, setup

DEPENDENCIES = ["nltk", "lxml"]
EXCLUDE_FROM_PACKAGES = ["contrib", "docs", "tests*"]
CURDIR = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(CURDIR, "README.md"), "r", encoding="utf-8") as f:
    README = f.read()


setup(
    name="norsecorpus",
    version="1.0.2",
    author="Clément Besnier",
    author_email="clemsciences@aol.com",
    description="Corpus of Old Norse texts with code to read them",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/clemsciences/old_norse_corpus",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    keywords=["old-norse", "corpus"],
    scripts=[],
    entry_points={"console_scripts": ["norsecorpus=norsecorpus.main:main"]},
    zip_safe=True,
    install_requires=DEPENDENCIES,
    test_suite="tests.test_project",
    python_requires=">=3.6",
    # license and classifier list:
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    license="License :: OSI Approved :: MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Markup :: XML"
        # "Private :: Do Not Upload"
    ],
)
