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