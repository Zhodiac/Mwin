#!/usr/bin/env python
from setuptools import setup, find_packages

long_description = read('README.txt','CHANGES.txt')
 
setup(

    name="Mwin",
    author="Zhodiac",
    version="0.10",
    license="LICENSE.txt",
    url="https://github.com/Zhodiac/Mwin",

    description="Places programs in certain layouts on screen for easy multitasking",
    long_description = long_description,
    packages=find_packages("."),
    install_requires = [
        "Tkinter"
    ],
)
