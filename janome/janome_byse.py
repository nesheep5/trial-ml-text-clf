import math, sys
from janome.tokenizer import Tokenizer

def getwords(doc):
    t = Tokenizer()
    torkens = t.tokenize(doc)
    
