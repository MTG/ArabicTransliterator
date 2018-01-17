#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='arabictransliterator',
      version='0.1',
      description='A code for transliterating (romanizing) Arabic text using the ALA-LC standard',
      author='CompMusic / MTG UPF',
      url='http://compmusic.upf.edu',
      packages=["mishkal", 'pyarabic', 'naftawayh', 'tashaphyne', 'qalsadi',"qalsadi.libqutrub","arabic"],
      package_dir={
              'tashaphyne':'tashaphyne',
              'naftawayh':'naftawayh',
              'pyarabic':'pyarabic',
              'qalsadi':'qalsadi',
              'libqutrub':'qalsadi/libqutrub',
              'arabic':'',
              'mishkal':'mishkal'}
)
