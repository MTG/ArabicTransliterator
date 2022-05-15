ArabicTransliterator
======

A code for transliterating (romanizing) Arabic text using the American Library Association - Library of Congress (ALA-LC) standard, but it can be extended
to any other Arabic standard. It uses the [mishkal library](https://github.com/linuxscout/mishkal) to vocalize/diacritize Arabic.

Dependencies
-------------
Most of the dependencies are already included in the code. The only additional dependency (in order to properly display Arabic characters in your screen) is:

+ [python-bidi](https://pypi.python.org/pypi/python-bidi)

Installation
------------
from inside the directory, run:

    python3 setup.py install
    pip3 install -e . 

How to use ArabicTransliterator
-------------------------------
Arabic Transliteration Example.ipynb is an example jupyter notebook that transliterates the files phrases.csv and nouns.csv
