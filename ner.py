# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 20:06:01 2022

@author: iammu
"""

modifiedHadithText = HadithText
    
from transformers import pipeline
pos = pipeline('token-classification', model='CAMeL-Lab/bert-base-arabic-camelbert-mix-pos-msa')
#text = 'إمارة أبوظبي هي إحدى إمارات دولة الإمارات العربية المتحدة السبع'
dummy = pos(modifiedHadithText)


nameList = []
name = ""
pre_end = 0
for j in range(len(dummy)):
    
    dic = dummy[j]
    
    if(dic.get("entity")=="noun_prop"):
        if(name=="" and pre_end==0):
            name = name +dic.get("word")
            pre_end = dic.get("end")
        else:
            if(dic.get("start")==pre_end):
                name = name + dic.get("word")
                pre_end = dic.get("end")
            else:
                name = name  + " " + dic.get("word")
                pre_end = dic.get("end")
    else:
        if(name!=""):  
            if(name.__contains__("#")):
                name = name.replace("#","")
            
            
            nameList.append(name.strip())
            name = ""
            pre_end=0