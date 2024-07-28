import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.corpus import stopwords
from unidecode import unidecode
from ForeignChars import checkForeignChars

nltk.download(['punkt', 'stopwords'])

def ReturnCleaned(method_instance):
    df = pd.read_csv('./spam.csv', encoding='ISO-8859-1')
    df = df[['v1', 'v2']]
    df.columns = ['class_labels', 'sms_text']
    vectoriser = method_instance
    vecs = vectoriser.fit_transform(df['sms_text']).toarray()

    df = pd.concat([df.reset_index(), pd.DataFrame(data=vecs, columns= vectoriser.get_feature_names_out(df['sms_text'])).reset_index()], axis=1)
    stop_words = set(stopwords.words())

    junk_columns = set(['index', 'level_0'])
    tokens = set(df.columns)

    for colname in tokens:
        if colname in stop_words:
            junk_columns.add(colname)

    df_new = df.drop(columns=list(junk_columns))

    new_tokens = set(df_new.columns)
    new_junk_columns = []

    for t in new_tokens:
        if checkForeignChars(t):
            new_junk_columns.append(t)

    new_junk_columns.remove('class_labels')
    new_junk_columns.remove('sms_text')

    df_new = df_new.drop(columns=new_junk_columns)
    return df_new

