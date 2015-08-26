#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='arabictransliterator',
      version='0.1',
      description='A code for transliterating (romanizing) Arabic text using the ALA-LC standard',
      author='CompMusic / MTG UPF',
      url='http://compmusic.upf.edu',
      packages=["tashkeel", "arabic"],
      package_dir={
              'tashaphyne':'tashaphyne',
              'naftawayh':'mishkal/lib/naftawayh', 
              'pyarabic':'mishkal/lib/pyarabic',
              'qalsadi':'mishkal/lib/qalsadi', 
              'libqutrub':'mishkal/lib/qalsadi/libqutrub',
              'arabic':'', 
              'tashkeel': 'mishkal/tashkeel' },

)
