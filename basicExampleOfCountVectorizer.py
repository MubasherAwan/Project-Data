# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 07:09:43 2022

@author: iammu
"""

from sklearn.feature_extraction.text import CountVectorizer
text = ["The quick brown fox jumped over the lazy dog fox dog.","Hello world"]
vectorizer = CountVectorizer()
vectorizer.fit(text)
print(vectorizer.vocabulary_)
vector = vectorizer.transform(text)
print(vector.shape)
print(type(vector))
print(vector.toarray())
