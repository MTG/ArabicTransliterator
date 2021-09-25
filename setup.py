#!/usr/bin/env python

from setuptools import setup, find_packages
import pkg_resources

with open("requirements.txt") as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

# Read meta-data
about = {}
exec(open('arabic_transliterator/__version.py').read(), about)

setup(name='arabic-transliterator',
      version=about["__version__"],
      description='A code for transliterating (romanizing) Arabic text using the ALA-LC standard',
      long_description=open("README.rst", encoding="utf-8").read(),
      long_description_content_type="text/x-rst",

      author='CompMusic / MTG UPF',
      url='http://compmusic.upf.edu',

      packages=["arabic_transliterator"],
      include_package_data=True,
      install_requires=install_requires,
      classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries"
      ],
)
