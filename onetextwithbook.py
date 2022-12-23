# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 10:01:19 2022

@author: hp
"""

import pandas as pd

dfc = pd.read_excel('''C:/Users/iammu/Bukhari's_Matan.xlsx''')
textm=list(dfc['Hadith_Matn'])
#text=[" يقرا بطول الطوليين    .", "  اذا نعس احدكم في الصلاة فلينم حتى يعلم ما يقرا    ."]

text1=[" ، قال :    اذا نعس احدكم في الصلاة فلينم حتى يعلم ما يقرا    ."
]
import nltk
from nltk.corpus import stopwords
arabicStopwords=stopwords.words('Arabic')
#print(arabicStopwords)


#__stopword Code
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
for i in range(len(textm)):
 # if(text1[0]==textm[i]):
    listRange=[]
    for i in range(len(textm)):
        listRange.append(str(i))
        
    from sklearn.feature_extraction.text import CountVectorizer
    import pandas as pd
    count_vectorizer = CountVectorizer(stop_words=(arabicStopwords))
    #count_vectorizer = CountVectorizer()
    print(count_vectorizer)
    sparse_matrix = count_vectorizer.fit_transform(textm)
    doc_term_matrix = sparse_matrix.todense()
    dfm = pd.DataFrame(doc_term_matrix, 
                      columns=count_vectorizer.get_feature_names(), 
                      index=listRange)
    #dfm
    
       
    listRange2=[]
    for i in range(len(text1)):
        listRange2.append(str(i))
    sparse_matrix2 = count_vectorizer.transform(text1)
    doc_term_matrix2 = sparse_matrix2.todense()
    df1 = pd.DataFrame(doc_term_matrix2, 
                      columns=count_vectorizer.get_feature_names(), 
                      index=listRange2)
    df1
    samilarity_matrix_matn=cosine_similarity(dfm, df1)
    print(samilarity_matrix_matn)

##########################################################
EqualToZero=[]
for i in range(len(samilarity_matrix_matn)):
    print(samilarity_matrix_matn[i])
    if(int(samilarity_matrix_matn[i][0])==0):
      EqualToZero.append(samilarity_matrix_matn[i][0])
      


# gzero=list(samilarity_matrix_matn)
# zero=[]   
# for i in range(len(gzero) ):
#     if(gzero[i]<1 and gzero!=0.):
#         print(gzero[i])
#         #gzero[i].append(zero)
# if ((samilarity_matrix_matn[dfm][df1]==0).all()):
#     gzero.append(samilarity_matrix_matn[dfm][df1])
    
 # else:
 #      print("not matched"); 