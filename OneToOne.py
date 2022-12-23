# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 13:22:57 2022

@author: iammu
"""

text=[" خياركم اسلاما احاسنكم اخلاقا اذا فقهوا"
    ,  " رضى الرب في رضى الوالد وسخط الرب في سخط الوالد"
," باي شيء كان يبدا رسول الله صلى الله عليه وسلم اذا دخل بيته؟ قالت : بالسواك . رواه مسلم" 
   ,"لولا ان اشق على امتي لامرتهم بالسواك عند كل صلاة"
 ]


text2=[" لولا ان اشق على امتي لامرتهم بالسواك عند كل صلاة"
    ,"رضى الرب في رضى الوالد وسخط الرب في سخط الوالد"," لعائشة باي شيء كان يبدا النبي صلى الله عليه وسلم اذا دخل بيته قالت بالسواك"
     ,"كنا جلوسا عند النبي صلی اللہ علیہ وسلم كانما على رءوسنا الطير ، ما يتكلم منا متكلم اذ جآءه اناس ، فقالوا : من احب عباد الله الى الله ؟ ، قال : احسنهم خلقا"
      ]


import nltk
from nltk.corpus import stopwords
arabicStopwords=stopwords.words('Arabic')
#print(arabicStopwords)


#____stopword Code
List=[]
for i in arabicStopwords:
    dummy = i
    dum1 = ""
    dum2 = ""
    outerFlag1=False
    outerFlag2=False
    outerFlag3=False
    if(dummy[0]=="ا"):
        outerFlag1=True
    if(dummy[0]=="إ"):
        outerFlag2=True
    if(dummy[0]=="أ"):
        outerFlag3=True
    if(outerFlag1):
        innerFlag=True
        for j in range(len(dummy)):
            if(dummy[j]=="ا" and innerFlag):
                dum1+="إ"
                dum2+="أ"
                innerFlag=False
            else:
                dum1+=dummy[j]
                dum2+=dummy[j]
    if(outerFlag2):
        innerFlag=True
        for j in range(len(dummy)):
            if(dummy[j]=="إ" and innerFlag):
                dum1+="ا"
                dum2+="أ"
                innerFlag=False
            else:
                dum1+=dummy[j]
                dum2+=dummy[j]
    if(outerFlag3):
        innerFlag=True
        for j in range(len(dummy)):
            if(dummy[j]=="أ" and innerFlag):
                dum1+="إ"
                dum2+="ا"
                innerFlag=False
            else:
                dum1+=dummy[j]
                dum2+=dummy[j]
    if(dum1 != "" and dum2 != ""):
        List.append(dum1)
        List.append(dum2)


arabicStopwords = arabicStopwords + List

arabicStopwords = list(dict.fromkeys(arabicStopwords))

#______



#print(ArabicStopwords)
#text.split()

#...........tokenize.......
print("text is:" +str(text))
spr=list(map(str.split,text))
print(str(spr))
#....................

#...........stopwordremove............
# without_stopwords=[]
# for word in str(spr):
#     if word not in arabicStopwords:
#         without_stopwords.append(word)
# print(without_stopwords)
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
count_vectorizer = CountVectorizer(stop_words=(arabicStopwords))
#count_vectorizer = CountVectorizer()
print(count_vectorizer)
sparse_matrix = count_vectorizer.fit_transform(text)
doc_term_matrix = sparse_matrix.todense()
df = pd.DataFrame(doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names(), 
                  index=['a','b','c','d'])
df

lst = []
for i in range(1,20):
    lst.append(i)

print (lst)
sparse_matrix2 = count_vectorizer.transform(text2)
doc_term_matrix2 = sparse_matrix2.todense()
df1 = pd.DataFrame(doc_term_matrix2, 
                  columns=count_vectorizer.get_feature_names(), 
                  index=['a','b','c','d'])
df1
# Compute Cosine Similarity
from sklearn.metrics.pairwise import cosine_similarity
samilarity_matrix=cosine_similarity(df, df1)
print(samilarity_matrix)
# import sentence_transformers
# from sentence_transformers import SentenceTransformer
# model = SentenceTransformer('bert-base-nli-mean-tokens')