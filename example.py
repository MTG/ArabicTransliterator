# -*- coding: utf-8 -*-

import codecs, platform
import arabic_reshaper #
from bidi.algorithm import get_display
from ALA_LC_Transliterator import ALA_LC_Transliterator
import sys
sys.path.append('mishkal/')
sys.path.append('mishkal/lib/')
import tashkeel.tashkeel as tashkeel

def print_reshape(text):
    """Reshapes arabic in order to display characters from right to left
    """
    if platform.system() == "Darwin":
        print text
    else:
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)
        print bidi_text

if __name__ == '__main__':
    f = codecs.open("example_arabic_script.dat", "r", "utf-8")
    transliterator = ALA_LC_Transliterator()
    for line in f:
        print "--------------Original Text--------------"
        text = line.strip()
        print_reshape(text)
        print "--------------Vocalized Text--------------"
        vocalizer=tashkeel.TashkeelClass()
        voc = vocalizer.tashkeel(text)
        print_reshape(voc)
        print "--------------Transliterated Text--------------"
        tr = transliterator.do(voc.strip())
        print_reshape(tr)
        print "#########################################"
    f.close()

