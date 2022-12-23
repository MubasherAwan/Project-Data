# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 20:39:54 2022

@author: iammu
"""


from sklearn import model_selection
import pandas as pd
import numpy as np




df2 = pd.read_csv("C:/Users/iammu/DataForMLModel.csv",encoding=('utf-8'))
# df2=pd.DataFrame()
df3 = pd.read_csv("C:/Users/iammu/OneDrive/Desktop/MLData/BukhariBooksDataForML.csv",encoding="utf-8")

arabicIsnadInBukhari = df3.Arabic_Isnad
arabicIsnadInBukhari = list(arabicIsnadInBukhari)
# df2.to_csv("C:/Users/iammu/DataForMLModel.csv")
# df2['Arabic_Isnad']=df.Arabic_Isnad
# df2['Arabic_Grade']=df.Arabic_Grade
from nltk.corpus import stopwords


#text1=df2.Arabic_Isnad[0]


# 
        #text="حَدَّثَنَا عَمْرُو بْنُ خَالِدٍ، قَالَ حَدَّثَنَا اللَّيْثُ، عَنْ يَزِيدَ، عَنْ أَبِي الْخَيْرِ، عَنْ عَبْدِ اللَّهِ بْنِ عَمْرٍو ـ رضى الله عنهما ـ"
text1=df2.Arabic_Isnad[1]
WithoutAhrabTxt=""
#finalText=' '

for  i in range(len(text1)):
    no=ord(text1[i])
    if(no==1614 or no==1615 or no==1616 or no==1618 or no==1617 or no==1612 or no==1613 or no==1611):
        continue
    else:
        WithoutAhrabTxt+=text1[i]
        
WordReplace=["حدثني","وحدثنا","حدثنا","نحوه","عن","قال","فقال","سمعت","يقول","أنه","سمع","أخبرني","مولى","أن","أخبرنا","اخبرنا","سال","قالت",":","قالا","جميعا","وحدثني","في حديثه","تابعه","انه","اخبرني","-"," ـ رضى الله عنهما","وعن","ـ رضى الله عنه"," ـ رضى الله عنها","حريثا","يحدث","ح","حدثتنا","حفص","لفظ","وهذا","هو","وهو","عنه","روى","متهما","صاحب","قيل","كان","حدثه","واحد","تلا","إنما","لعن",'كان',"بهز","رواية","لما","مر","قال","عليا","حدثته","له","أنها","‏.‏","وقد","روي","من","كنت","كهمس","وأخبرني"]
RA_List = ['رضى الله عنهما','رضى الله عنه','رضى الله عنها','رضي الله عنه',"ح‏.‏ "]

STOPWORDS = set(stopwords.words('arabic'))
# dummy= list(STOPWORDS)
tokenList=WithoutAhrabTxt.split()
newList = [word for word in tokenList if word not in STOPWORDS]

newtext = ' '.join(newList)


finalTokenList = newtext.split("،")


for i in range(len(finalTokenList)):
    finalTokenList[i] = finalTokenList[i].strip()
    
    for j in range(len(RA_List)):
        if(finalTokenList[i].__contains__(RA_List[j])):
            finalTokenList[i] = finalTokenList[i].replace(RA_List[j], "")
            
    finalTokenList[i] = finalTokenList[i].strip()
    
    
for i in range(len(finalTokenList)):
    for j in range(len(WordReplace)):
        if(finalTokenList[i].__contains__(WordReplace[j])):
            finalTokenList[i] = finalTokenList[i].replace(WordReplace[j],"")
            finalTokenList[i] =finalTokenList[i].strip()





# dumForBukhari= df3['Arabic_Isnad'].apply(clean_text)     
    
