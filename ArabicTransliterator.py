
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
            if self.table.has_key(c): trans_data += self.table[c]
            else: trans_data += '[UNK]'
        return trans_data