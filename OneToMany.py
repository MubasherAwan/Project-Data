# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 13:26:15 2022

@author: iammu
"""


import pandas as pd

dfc = pd.read_csv('C:/Users/iammu/OneDrive/Desktop/PyhtonProgram/matn.csv',encoding="utf-8")
textm=list(dfc['Hadith_Matn'])

text=["  , قال :    ليس فيما دون خمسة اوسق من التمر صدقة ، وليس فيما دون خمس اواق من الورق صدقة ، وليس فيما دون خمس ذود من الابل صدقة    ."
]

import nltk
from nltk.corpus import stopwords
arabicStopwords=stopwords.words('Arabic')
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

from sklearn.metrics.pairwise import cosine_similarity
# for i in range(len(textm)):
#     if(text[0]==textm[i]):
       
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
count_vectorizer = CountVectorizer(stop_words=(arabicStopwords))
#count_vectorizer = CountVectorizer()
print(count_vectorizer)
sparse_matrix = count_vectorizer.fit_transform(textm)
doc_term_matrix = sparse_matrix.todense()
listRange=[]
for i in range(len(textm)):
    listRange.append(str(i))
dfm = pd.DataFrame(doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names(), 
                  index=listRange)

sparse_matrix2 = count_vectorizer.transform(text)
doc_term_matrix2 = sparse_matrix2.todense()
listRange2=[]
for i in range(len(text)):
    listRange2.append(str(i))
df1 = pd.DataFrame(doc_term_matrix2, 
                  columns=count_vectorizer.get_feature_names(), 
                  index=listRange2)
df1
   
samilarity_matrix_matn=cosine_similarity(dfm, df1)
print(samilarity_matrix_matn)
    
EqualToone=[]
for i in range(len(samilarity_matrix_matn)):
    #print(samilarity_matrix_matn[i])
    if(int(samilarity_matrix_matn[i][0])==1):
      EqualToone.append(samilarity_matrix_matn[i][0] ) 
      print ("Index Number","\n",i,"\n", "Similarity between Ahadith is :", "\n", samilarity_matrix_matn[i][0],"\n","Matching Ahadith is", "\n",  textm[i])
      
lesstoone=[]
for i in range(len(samilarity_matrix_matn)):
    #print(samilarity_matrix_matn[i])
    if(int(samilarity_matrix_matn[i][0])<=1 and samilarity_matrix_matn[i][0]!=0.):
      lesstoone.append(samilarity_matrix_matn[i][0]) 
      print ("Index Number","\n",i,"\n", "Similarity between Ahadith is :", "\n", samilarity_matrix_matn[i][0],"\n","Matching Ahadith is", "\n",  textm[i])
      
Equaltozero=[]
for i in range(len(samilarity_matrix_matn)):
    #print(samilarity_matrix_matn[i])
    if(samilarity_matrix_matn[i][0]>=0.6):
      Equaltozero.append(samilarity_matrix_matn[i][0]) 
      print ("Index Number","\n",i,"\n", "Similarity between Ahadith whose similarity is greater or equal to 0.6 :", "\n", samilarity_matrix_matn[i][0],"\n","Matching Ahadith is", "\n",  textm[i])
      
# indexbased=[]
# if(samilarity_matrix_matn[i][0]==textm[i]):

#     indexbased.append(samilarity_matrix_matn[i][0])
#     print(textm[i])