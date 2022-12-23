# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 17:10:56 2022

@author: iammu
"""

"""
Created on Thu Jun 23 19:14:16 2022

@author: iammu
"""





# import mysql.connector

# myDb = mysql.connector.connect(host="localhost", user="root", passwd="fb834946220403", database="sihah_al_sittah")
# myCursor = myDb.cursor()

# isnadTrainingList = []

# gradeTrainingList = []

# query1 = "select arabic_isnad,arabic_grade from bukhari_book where arabic_grade='صحيح';"
# myCursor.execute(query1)
# result1 = myCursor.fetchall()

# print(len(result1))
# for i in range(len(result1)):
#     isnadTrainingList.append(result1[i][0])
#     gradeTrainingList.append(result1[i][1])

# query2 = "select arabic_isnad,arabic_grade from muslim_book where arabic_grade='صحيح';"
# myCursor.execute(query2)
# result2 = myCursor.fetchall()

# print(len(result2))
# for i in range(len(result2)):
#     isnadTrainingList.append(result2[i][0])
#     gradeTrainingList.append(result2[i][1])
    

# query3 = "select arabic_isnad,arabic_grade from ibnMaja_book where arabic_grade='صحيح';"
# myCursor.execute(query3)
# result3 = myCursor.fetchall()

# print(len(result3))
# for i in range(len(result3)):
#     isnadTrainingList.append(result3[i][0])
#     gradeTrainingList.append(result3[i][1])



# query4 = "select arabic_isnad,arabic_grade from ibnMaja_book where arabic_grade='حسن';"
# myCursor.execute(query4)
# result4 = myCursor.fetchall()

# print(len(result4))
# for i in range(len(result4)):
#     isnadTrainingList.append(result4[i][0])
#     gradeTrainingList.append(result4[i][1])



# query5 = "select arabic_isnad,arabic_grade from ibnMaja_book where arabic_grade='ضعيف';"
# myCursor.execute(query5)
# result5 = myCursor.fetchall()

# print(len(result5))
# for i in range(len(result5)):
#     isnadTrainingList.append(result5[i][0])
#     gradeTrainingList.append(result5[i][1])



# query6 = "select arabic_isnad,arabic_grade from tirmizi_book where arabic_grade='صحيح';"
# myCursor.execute(query6)
# result6 = myCursor.fetchall()

# print(len(result6))
# for i in range(len(result6)):
#     isnadTrainingList.append(result6[i][0])
#     gradeTrainingList.append(result6[i][1])



# query7 = "select arabic_isnad,arabic_grade from tirmizi_book where arabic_grade='حسن';"
# myCursor.execute(query7)
# result7 = myCursor.fetchall()

# print(len(result7))
# for i in range(len(result7)):
#     isnadTrainingList.append(result7[i][0])
#     gradeTrainingList.append(result7[i][1])



# query8 = "select arabic_isnad,arabic_grade from tirmizi_book where arabic_grade='ضعيف';"
# myCursor.execute(query8)
# result8 = myCursor.fetchall()

# print(len(result8))
# for i in range(len(result8)):
#     isnadTrainingList.append(result8[i][0])
#     gradeTrainingList.append(result8[i][1])



# query9 = "select arabic_isnad,arabic_grade from abuDaud_book where arabic_grade='صحيح';"
# myCursor.execute(query9)
# result9 = myCursor.fetchall()

# print(len(result9))
# for i in range(len(result9)):
#     isnadTrainingList.append(result9[i][0])
#     gradeTrainingList.append(result9[i][1])



# query10 = "select arabic_isnad,arabic_grade from abuDaud_book where arabic_grade='صحيح موقوف';"
# myCursor.execute(query10)
# result10 = myCursor.fetchall()

# print(len(result10))
# for i in range(len(result10)):
#     isnadTrainingList.append(result10[i][0])
#     gradeTrainingList.append('صحيح')



# query11 = "select arabic_isnad,arabic_grade from abuDaud_book where arabic_grade='صحيح مقطوع';"
# myCursor.execute(query11)
# result11 = myCursor.fetchall()

# print(len(result11))
# for i in range(len(result11)):
#     isnadTrainingList.append(result11[i][0])
#     gradeTrainingList.append('صحيح')



# query12 = "select arabic_isnad,arabic_grade from abuDaud_book where arabic_grade='حسن';"
# myCursor.execute(query12)
# result12 = myCursor.fetchall()

# print(len(result12))
# for i in range(len(result12)):
#     isnadTrainingList.append(result12[i][0])
#     gradeTrainingList.append(result12[i][1])



# query13 = "select arabic_isnad,arabic_grade from abuDaud_book where arabic_grade='ضعيف';"
# myCursor.execute(query13)
# result13 = myCursor.fetchall()

# print(len(result13))
# for i in range(len(result13)):
#     isnadTrainingList.append(result13[i][0])
#     gradeTrainingList.append(result13[i][1])



# query14 = "select arabic_isnad,arabic_grade from abuDaud_book where arabic_grade='شاذ';"
# myCursor.execute(query14)
# result14 = myCursor.fetchall()

# print(len(result14))
# for i in range(len(result14)):
#     isnadTrainingList.append(result14[i][0])
#     gradeTrainingList.append('ضعيف')



# query15 = "select arabic_isnad,arabic_grade from abuDaud_book where arabic_grade='منكر';"
# myCursor.execute(query15)
# result15 = myCursor.fetchall()

# print(len(result15))
# for i in range(len(result15)):
#     isnadTrainingList.append(result15[i][0])
#     gradeTrainingList.append('ضعيف')



# query16 = "select arabic_isnad,arabic_grade from nesai_book where arabic_grade='صحيح';"
# myCursor.execute(query16)
# result16 = myCursor.fetchall()

# print(len(result16))
# for i in range(len(result16)):
#     isnadTrainingList.append(result16[i][0])
#     gradeTrainingList.append(result16[i][1])



# query17 = "select arabic_isnad,arabic_grade from nesai_book where arabic_grade='حسن';"
# myCursor.execute(query17)
# result17 = myCursor.fetchall()

# print(len(result17))
# for i in range(len(result17)):
#     isnadTrainingList.append(result17[i][0])
#     gradeTrainingList.append(result17[i][1])



# query18 = "select arabic_isnad,arabic_grade from nesai_book where arabic_grade='ضعيف';"
# myCursor.execute(query18)
# result18 = myCursor.fetchall()

# print(len(result18))
# for i in range(len(result18)):
#     isnadTrainingList.append(result18[i][0])
#     gradeTrainingList.append(result18[i][1])

# import pandas as pd
# df1 = pd.DataFrame()
# df1["arabic_isnad"] = arabicIsnadInBukhari
# df1["arabic_grade"] = arabicGradeInBukhari

# df1.to_csv("C:/Users/iammu/OneDrive/Desktop/DataForMachineLearning.csv")


from sklearn import model_selection
import pandas as pd
import numpy as np
import collections

# Code For BOW
# df2 = pd.read_csv("C:/Users/iammu/DataForMLModel.csv",encoding=('utf-8'))
# df2=pd.DataFrame()
df = pd.read_csv("C:/Users/iammu/OneDrive/Desktop/DataForMachineLearning.csv",encoding="utf-8")

arabicIsnads = df.arabic_isnad
arabicIsnads = list(arabicIsnads)

arabicGrades = df.arabic_grade
arabicGrades = list(arabicGrades)
# df2.to_csv("C:/Users/iammu/DataForMLModel.csv")
# df2['Arabic_Isnad']=df.Arabic_Isnad
# df2['Arabic_Grade']=df.Arabic_Grade
from nltk.corpus import stopwords


#text1=df2.Arabic_Isnad[0]

def clean_text(text):

# 
        #text="حَدَّثَنَا عَمْرُو بْنُ خَالِدٍ، قَالَ حَدَّثَنَا اللَّيْثُ، عَنْ يَزِيدَ، عَنْ أَبِي الْخَيْرِ، عَنْ عَبْدِ اللَّهِ بْنِ عَمْرٍو ـ رضى الله عنهما ـ"
    text1=text
    WithoutAhrabTxt=""
    finalText=' '
    
    for  i in range(len(text1)):
        no=ord(text1[i])
        if(no==1614 or no==1615 or no==1616 or no==1618 or no==1617 or no==1612 or no==1613 or no==1611):
            continue
        else:
            WithoutAhrabTxt+=text1[i]
            
    WordReplace=["حدثني","وحدثنا","حدثنا","نحوه","قال","فقال","سمعت","يقول","سمع","أخبرني","مولى","أخبرنا","اخبرنا","قالت",":","قالا","جميعا","وحدثني","في حديثه","تابعه","اخبرني","حريثا","يحدث","حدثتنا","حفص","لفظ","وهذا","روى","متهما","صاحب","قيل","كان","حدثه","واحد","تلا","إنما","لعن",'كان',"رواية","قال","عليا","حدثته","أنها","‏.‏","وقد","روي","أخبره","كنت","وأخبرني"]
    RA_List = ['رضى الله عنهما','رضى الله عنه','رضى الله عنها','رضي الله عنه',"ح‏.‏ "]
    
    STOPWORDS = set(stopwords.words('arabic'))
    dummy= list(STOPWORDS)
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
    
        
    
    
    return(finalTokenList)

# dumForBukhari= df3['Arabic_Isnad'].apply(clean_text)     
    
dum = df['arabic_isnad'].apply(clean_text)
dum=list(dum)





# #________Check Float value in Book____
# for i in range(len(arabicIsnadInBukhari)):
#     if(type(df3.Arabic_Grade[i]).strip()!=""):
#         print(i)
        

# #_____________

#___Without Comma Isnad______
# count=0
# withCommaLists = []
# for i in range(len(dum)):
#     if(dum[i].__contains__('،')):
#         # withCommaLists.append(dum[i])
#         continue
#     else:
#         count+=1
        # withoutCommaList.append(df2.Arabic_Isnad[i])
        # print(i)
    
#__________





# import re
# def tokenizer(isnads):
#     for isnad in isnads:
#         name = re.split('، |_|-|! .', isnad)
#         for nam in name:
#             BagOfName.append(nam)

BagOfName=[]                  
for i in range(len(dum)):
    for name in dum[i]:
        BagOfName.append(name)

#______Step 2
#...Removing Null Index....
while("" in BagOfName) :
    BagOfName.remove("")
    
#Removing Duplicate
BagOfName = list(set(BagOfName))  

#Removing spaces from strating and from ending
for i in range(len(BagOfName)):
    BagOfName[i]=BagOfName[i].strip()
    
# #__________BON End
# dumDf=pd.DataFrame()
# dumDf["Names"]=BagOfName
# dumDf.to_csv("C:/Users/iammu/OneDrive/Desktop/BAG_Of_Name_New.csv")

#____________________________________
# End of BOW code


# countVect_BON = []
# countVect_BON2 = []
# countVect_DF = pd.DataFrame()

# def calculateBOW(wordset,l_doc):
#     tf_diz = dict.fromkeys(wordset,0)
#     for word in wordset:
#         tf_diz[word] = l_doc.count(tf_diz[word])
#     return tf_diz

# for i in range(len(arabicIsnads)):
#     if(i<16000):
#         countVect_BON.append(calculateBOW(BagOfName, dum[i]))
#     else:
#         countVect_BON2.append(calculateBOW(BagOfName, dum[i]))
    
# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(arabicIsnads)
# # vectorizer.get_feature_names_out()
# #array(BagOfName)
# # print(X.toarray())

# df_bon_Sklearn = pd.DataFrame(X.toarray(),columns=vectorizer.get_feature_names())

# df_bon_Sklearn.head()

# vectorizer_IDF = TfidfVectorizer()
# response = vectorizer_IDF.fit_transform(arabicIsnads)
# df_tfidf_Sklearn = pd.DataFrame(response.toarray(),columns = vectorizer_IDF.get_feature_names())

# df_tfidf_Sklearn.head()


# clf = LogisticRegression.fit(X,Y) 
# clf.predict(X_test) 

# clf.predict_proba(X_test)
# clf.score(X, Y)
# print("Logistic Regression")
# print(accuracy_score(Y_pred,Y_test))


# from sklearn.metrics import confusion_matrix

# #Generate the confusion matrix
# cf_matrix = confusion_matrix(Y_test, Y_pred)

# print(cf_matrix)

