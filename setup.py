#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='arabictransliterator',
      version='0.3',
      description='A code for transliterating (romanizing) Arabic text using the ALA-LC standard',
      author='CompMusic / MTG UPF',
      url='http://compmusic.upf.edu',
      include_package_data=True,
      packages=['aranasyn', 'arramooz', 'asmai', 'collocations', 'collocations.pyarabic', 'mishkal', 'mishkal.tashkeel', 'pyarabic', 'naftawayh', 'tashaphyne', 'qalsadi', 'qalsadi.libqutrub', 'arabic', 'CodernityDB'],

      package_dir={
              'tashaphyne':'tashaphyne',
              'naftawayh':'naftawayh',
              'pyarabic':'pyarabic',
              'qalsadi':'qalsadi',
              'libqutrub':'qalsadi/libqutrub',
              'arabic':'',
              'mishkal':'mishkal'},

      package_data={
              'arramooz': ['data/*'],
              'collocations': ['data/*']}
)
