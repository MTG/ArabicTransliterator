#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='arabictransliterator',
      version='0.1',
      description='A code for transliterating (romanizing) Arabic text using the ALA-LC standard',
      author='CompMusic / MTG UPF',
      url='http://compmusic.upf.edu',
      packages=["tashkeel"],
      install_requires=['Tashaphyne', 'Qalsadi', 'PyArabic', 'Naftawayh==0.1'],
      package_dir={'tashkeel': 'mishkal/tashkeel', 'libqutrub':'mishkal/lib/qalsadi/libqutrub'},
)
