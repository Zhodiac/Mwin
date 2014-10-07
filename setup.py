#!/usr/bin/env python
from setuptools import setup, find_packages

setup(

    name="Mwin",
    author="Zhodiac",
    version="0.10",
    license="LICENSE.txt",
    url="https://github.com/Zhodiac/Mwin",

    description="Places programs in certain layouts on screen for easy multitasking",
    packages=find_packages("."),
    install_requires = [
        "Tkinter"
    ],
)
