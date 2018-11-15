#key value model structure used by factory
class KeyValue(object):
    def __init__(self, keyRec, valRec):
        self.keyRec = keyRec
        self.valRec = valRec

    def __str__(self):
        return '%s:%s' % (self.keyRec, self.valRec)
