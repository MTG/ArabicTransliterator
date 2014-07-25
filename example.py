# -*- coding: utf-8 -*-

# This file is part of ArabicTransliterator.
#
# ArabicTransliterator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ArabicTransliterator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ArabicTransliterator.  If not, see <http://www.gnu.org/licenses/>.

# Written by Mohamed Sordo (@neomoha)
# Email: mohamed ^dot^ sordo ^at^ gmail ^dot^ com
# Website: http://msordo.weebly.com

import codecs, platform
import arabic_reshaper #
from bidi.algorithm import get_display
from ALA_LC_Transliterator import ALA_LC_Transliterator
import sys
sys.path.append('mishkal/')
sys.path.append('mishkal/lib/')
import tashkeel.tashkeel as tashkeel

def reshape(text):
    """Reshapes arabic in order to display characters from right to left
    """
    if platform.system() == "Darwin":
        return text
    else:
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)
        return bidi_text

if __name__ == '__main__':
    f = codecs.open("example_arabic_script.dat", "r", "utf-8")
    transliterator = ALA_LC_Transliterator()
    for line in f:
        print "--------------Original Text--------------"
        text = line.strip()
        print reshape(text)
        print "--------------Vocalized Text--------------"
        vocalizer=tashkeel.TashkeelClass()
        voc = vocalizer.tashkeel(text)
        print reshape(voc)
        print "--------------Transliterated Text--------------"
        tr = transliterator.do(voc.strip())
        print reshape(tr)
        print "#########################################"
    f.close()

