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

import string

class ArabicTransliterator:
    """Arabic Transliterator Base Class
    """
    def __unicode__(self):
        return u"Arabic Transliterator Base Class"
    
    def __load_dictionary(self):
        pass
    
    def do(self, data):
        #print self.table.items()
        #return data.translate(self.table)
        trans_data = u""
        for c in data:
            if c in self.table: trans_data += self.table[c]
            else: trans_data += '[UNK]'
        return trans_data

class ALA_LC_Transliterator(ArabicTransliterator):
    """Arabic Transliterator using the American Library Association - Library of Congress (ALA-LC) romanization standard
    """
    def __init__(self):
        self.invtable = {}
        self.table = {}
        self.__load_dictionary()

    def __unicode__(self):
        return u"Arabic ALA-LC Transliterator"

    def __load_dictionary(self):
        self.invtable = {u"\u2019": u"\u0621", # hamza-on-the-line
            u"\u0101": u"\u0622", # madda
            #u">": u"\u0623", # hamza-on-'alif # SPECIAL CASE
            #u"&": u"\u0624", # hamza-on-waaw # SPECIAL CASE
            #u"<": u"\u0625", # hamza-under-'alif # SPECIAL CASE
            #u"}": u"\u0626", # hamza-on-yaa' # SPECIAL CASE
            #u"A": u"\u0627", # bare 'alif # SPECIAL CASE
            u"b": u"\u0628", # baa'
            #u"p": u"\u0629", # taa' marbuuTa # SPECIAL CASE
            u"T": u"\u062A", # taa' # SPECIAL upper case to distinguis ending of words with taa' marbuuta
            u"th": u"\u062B", # thaa'
            u"j": u"\u062C", # jiim
            u"\u1E25": u"\u062D", # Haa'
            u"kh": u"\u062E", # khaa'
            u"d": u"\u062F", # daal
            u"dh": u"\u0630", # dhaal
            u"r": u"\u0631", # raa'
            u"z": u"\u0632", # zaay
            u"s": u"\u0633", # siin
            u"sh": u"\u0634", # shiin
            u"\u1E63": u"\u0635", # Saad
            u"\u1E0D": u"\u0636", # Daad
            u"\u1E6D": u"\u0637", # Taa'
            u"\u1E93": u"\u0638", # Zaa' (DHaa')
            u"\u2018": u"\u0639", # cayn
            u"gh": u"\u063A", # ghayn
            #u"_": u"\u0640", # taTwiil
            u"f": u"\u0641", # faa'
            u"q": u"\u0642", # qaaf
            u"k": u"\u0643", # kaaf
            #u"l": u"\u0644", # laam # SPECIAL CASE
            u"m": u"\u0645", # miim
            u"n": u"\u0646", # nuun
            u"h": u"\u0647", # haa'
            #u"w": u"\u0648", # waaw #SPECIAL CASE
            #u"Y": u"\u0649", # 'alif maqSuura # SPECIAL CASE
            #u"y": u"\u064A", # yaa' #SPECIAL CASE
            u"an": u"\u064B", # fatHatayn
            u"un": u"\u064C", # Dammatayn
            u"in": u"\u064D", # kasratayn
            #u"a": u"\u064E", # fatHa #SPECIAL CASE
            u"u": u"\u064F", # Damma
            u"i": u"\u0650", # kasra
            #u"~": u"\u0651", # shaddah # SPECIAL CASE
            u"": u"\u0652", # sukuun
            #u"`": u"\u0670", # dagger 'alif
            #u"{": u"\u0671", # waSla
            u" ": u" ",
        }
        # For a reverse transliteration (Unicode -> ALA-LC), a dictionary
        # which is the reverse of the above alalc2uni is essential.
        self.table = {}
        # Iterate through all the items in the alalc2uni dict.
        for (key, value) in self.invtable.items():
            self.table[value] = key

    def do(self, data):
        trans_data = u""
        #print `data[:]`
        #multi_character_translation = dict([(k,v) for k,v in self.table.iteritems() if len(v) > 1])
        for i in range(len(data)):
            if data[i] in self.table:
                trans_data += self.table[data[i]]
            #----------- SPECIAL CASES -----------
            else:
                if data[i] == u"\u0627": # BARE 'ALIF - RULES 1, 2 and 5
                    #print `data[:]`
                    if len(data) > i+1 and data[i+1] == u"\u0644" and (i==0 or (i>0 and data[i-1] == ' ')): # laam at the beggining of a word
                        trans_data += u"a"
                    elif i == 0: # Alif as first character
                        continue # don't add anything
                    elif (i==2 and data[i-2:i] in (u"\u0628\u0650", u"\u0644\u0650")) or (i>2 and data[i-3:i] in (u" \u0628\u0650", u" \u0644\u0650")): #'ALIF preceded by prepositions "bi" or "li" RULES 10 and 17b
                        if len(data) > i+1 and data[i+1] == u"\u0644":
                            trans_data += "-a"
                        else:
                            trans_data += "-"
                    elif i>0 and data[i-1] == u"\u064E": # fatHa
                        trans_data = trans_data[:-1]+u"\u0101" # long fatha
                    elif i>1 and data[i-1] == u"\u0652" and data[i-2] == u"\u0644": # sukuun laam
                        continue # don't add anything
                    elif i>0 and data[i-1] == u"\u064B": # fatHatayn
                        continue # don't add anything
                    else:
                        trans_data += u"\u0101"

                elif data[i] == u"\u064A": # YAA' - RULES 1, 2 and 4
                    #print `data[:]`
                    #if i>0 and data[i-1] == u"\u0650" or (i>1 and data[i-2] not in (u"\u064E", u"\u064F")) and ((len(data)>i+1 and data[i+1] not in (u"\u064E", u"\u064F", u"\u0650")) or len(data) == i+1): # kasra
                    if i>0 and data[i-1] == u"\u0650": #kasra
                        if i>1 and data[i-2] in (u"\u064E", u"\u064F"): # fatha, damma / rare case
                            trans_data = trans_data[:-1]+u"y"
                        elif len(data)>i+1 and data[i+1] in (u"\u064E", u"\u064F", u"\u0650"): # fatha, damma, kasra
                            trans_data += u"y"
                        else:
                            trans_data = trans_data[:-1]+u"\u012B" #long kasra
                    elif i>0 and data[i-1] not in (u"\u064E", u"\u064F", u"\u0627") and ((len(data)>i+1 and data[i+1] not in (u"\u064E", u"\u064F", u"\u0650")) or len(data) == i+1):
                        # yaa' (not preceeded by fatha/damma or bare 'alif) and (not suceeded by vowel or it's end of word)
                        if len(data) > i+1 and data[i+1] in (u"\u0627"): #succeeded by alif and fatha omitted
                            trans_data += u"y"
                        else:
                            trans_data += u"\u012B" #long kasra
                    else:
                        trans_data += u"y"

                elif data[i] == u"\u0648": # WAAW - RULES 1, 2 and 4
                    if i>0 and data[i-1] == u"\u064F" and ((len(data)==i+1) or (len(data)>i+1 and data[i+1] not in (u"\u064E", u"\u0650"))): # damma
                        trans_data = trans_data[:-1]+u"\u016B" #long damma
                    elif i>0 and data[i-1] not in (u"\u064E", u"\u064F", u"\u0650", u"\u0652", u" "): # fatha, damma, kasra, sukun, space
                        if len(data) > i+1 and data[i+1] in (u"\u064E", u"\u064F", u"\u0650"):
                            trans_data += u"w"
                        else:
                            trans_data += u"\u016B" #long damma
                        #TODO: case when waaw is preceeded by 'ALIF
                        #if (i==1) or (i>2 and data[i-3:i] != u"\u0627\u0644\u0652"): # not preceeded by bare 'alif + lam + sukun
                        #    trans_data += u"\u016B" #long damma
                        #else:
                        #    trans_data += u"w"
                    else:
                        trans_data += u"w"

                elif data[i] == u"\u0644": # LAAM
                    if i>0 and data[i-1] == u"\u0627": # bare 'alif at the beggining
                        if (i==1 or (i>1 and data[i-2]==u" ")):
                            trans_data += u"l-"
                        # waaw + bare 'alif at the beginning
                        elif (i==3 and data[i-3:i]==u"\u0648\u064E\u0627") or (i>3 and data[i-4:i]==u" \u0648\u064E\u0627"):
                            trans_data += u"l-"
                        elif len(trans_data) > 3 and trans_data[-2] == u"-": # RULES 10 and 17b
                            trans_data += u"l-"
                        else:
                            trans_data += u"l"
                    else:
                        trans_data += u"l"

                elif data[i] == u"\u0629": # TAA' MARBUUTA - RULE 7
                    if len(data) > i+3 and data[i+1:i+4] == u" \u0627\u0644": # space + laam + 'alif
                        trans_data += u"t"
                    elif len(data) > i+4 and data[i+1] in (u"\u064E", u"\u064F", u"\u0650") and data[i+2:i+5] == u" \u0627\u0644": # fatha/damma/kasra + space + laam + 'alif
                        trans_data += u"t"
                    elif len(data) > i+1 and data[i+1] in (u"\u064B", u"\u064C", u"\u064D"): # fatHatayn, Dammatayn, kasratayn
                        trans_data += u"t"
                    else:
                        trans_data += u"h"

                elif data[i] == u"\u0649": # 'ALIF MAQSUURA - RULE 6
                    if i>0 and data[i-1] == u"\u064E": # fatHa
                        trans_data = trans_data[:-1]+u"\u00E1" # long fatha but with alif maqSuura
                    elif i > 0 and data[i-1] == u"\u064B": #fatHatayn
                        continue # don't add anything
                    else:
                        trans_data += u"\u00E1"

                elif data[i] in (u"\u0623", u"\u0624", u"\u0625", u"\u0626"): # HAMZA-ON-'ALIF, HAMZA-ON-WAAW, HAMZA-UNDER-'ALIF, HAMZA-ON-YAA' - RULE 8
                    if i==0 or (i>0 and data[i-1] == " ") or (i>1 and data[i-2:i] == u"\u0627\u0644") or (i>2 and data[i-3:i] == u"\u0627\u0644\u0652"): # hamza at the begigging or preceeded by al- or al- plus sukun
                        continue # don't add anything
                    else:
                        trans_data += u"\u2019"


                elif data[i] == u"\u064E": # FATHA
                    if i>0 and data[i-1] == u"\u0627": # bare 'alif
                        continue # don't add anything
                    else:
                        trans_data += 'a'

                elif data[i] == u"\u0651": #SHADDA - RULE 11
                    if i>0 and data[i-1] not in (u"\u064A", u"\u0648"): # not yaa' nor waaw' --> double character
                        if i>2 and data[i-3:i-1] == u"\u0627\u0644": # if shadda is preceeded by al-
                            continue # don't add anything
                        elif i>1 and data[i-2:i] == u"\u0627\u0644": # if shadda is over the l of al-:
                            trans_data += "l"
                        elif data[i-1] in self.table:
                            trans_data += self.table[data[i-1]]
                        else:
                            trans_data += trans_data[-1]
                    elif i>1 and data[i-1] == u"\u0648": # waaw --> TODO: nothing special here
                        trans_data += "w"
                    elif i>1 and data[i-1] == u"\u064A": # yaa'
                        if data[i-2] == u"\u0650" and len(data) == i+1 or (len(data) == i+2 and data[i+1] in (u"\u064E", u"\u064F", u"\u0650")) or (len(data) > (i+2) and data[i+2]==u" "): #final yaa' preceeded by kasra
                            continue # don't add anything
                        else:
                            trans_data += "y"
                elif data[i] in string.punctuation or data[i].isdigit(): # don't trasnliterate punctuation marks and digits
                    trans_data += data[i]
                else:
                    trans_data += u"[UNK]"
        ret_data = []
        # IGNORE LAST DIACRITIC + POST-PROCESSING
        for word in trans_data.strip().split(" "):
            if len(word) > 0:
                if word[-1] in (u"a", u"u", u"i"):
                    word = word[:-1]
                    if len(word) > 1 and word[-2:] == "iy":
                        word = word[:-2]+u"\u012B"
                if word.startswith(u"w"+u"\u0101"+u"l-"): # conjunction waaw joined into another word
                    word = u"wal-"+word[4:]
                if len(word) > 0 and word[-1] == u"t" and (word.startswith(u"al-") or word.startswith(u"wal-")):
                    word = word[:-1]+u"h"
                word = word.replace(u"T", u"t") # taa maftou7a, back to lower case
                ret_data.append(word)
        return u" ".join(ret_data)
