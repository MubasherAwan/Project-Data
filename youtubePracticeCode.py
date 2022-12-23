# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 13:57:33 2022

@author: iammu
"""

from nltk.corpus import stopwords
import re
import pandas as pd
df = pd.read_csv('C:/Users/iammu/OneDrive/Desktop/cuisineDatasetForML.csv')
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score

len(df.cuisine.value_counts())

df.cuisine.unique()


df.isnull().sum()

df.shape

df.drop_duplicates(inplace=True)

df.shape


print(df['cuisine_description'].apply(lambda x: len(x.split(' '))).sum())

special_character_remover = re.compile('[/(){}\[\]\|@,;]')
extra_symbol_remover = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))
def clean_text(text):
    text = text.lower()
    text = special_character_remover.sub(' ', text)
    text = extra_symbol_remover.sub('', text)
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)
    return text
    
df['cuisine_description'] = df['cuisine_description'].apply(clean_text)
print(df['cuisine_description'].apply(lambda x: len(x.split(' '))).sum())



from sklearn.model_selection import train_test_split
X = df.cuisine_description
y = df.cuisine
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 42)
X_train.shape,X_test.shape,y_train.shape,y_test.shape


from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer

lr = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', LogisticRegression()),
              ])

lr.fit(X_train,y_train)
y_pred1 = lr.predict(X_test)

print(f"Accuracy is : {accuracy_score(y_pred1,y_test)}")



from sklearn.naive_bayes import MultinomialNB


naivebayes = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])
naivebayes.fit(X_train, y_train)

y_pred = naivebayes.predict(X_test)

print(f'accuracy {accuracy_score(y_pred,y_test)}')





