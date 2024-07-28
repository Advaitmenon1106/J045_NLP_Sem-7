import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def checkForeignChars(token: str):
    for letter in set(token):
        if ord(letter) not in range(65, 65+26) and ord(letter) not in range(97, 97+26):
            return True
    return False