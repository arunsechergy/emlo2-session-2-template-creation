#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="src",
    version="0.0.1",
    description="Tech Stack for Deep Learning Prototyping",
    author="arunsechergy",
    author_email="arunkumar.rn.eee@gmail.com",
    url="https://github.com/arunsechergy/emlo2-session-2-template-creation", 
    install_requires=["pytorch-lightning", "hydra-core"],
    packages=find_packages(),
)
