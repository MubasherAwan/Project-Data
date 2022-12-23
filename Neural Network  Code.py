# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:44:46 2022

@author: iammu
"""

import pandas as pd
import numpy as np
import mysql.connector

# df = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/comparison/CombinedRuleBasedAndNewNERWithExactNames/NamesAndLengthComparison_RuleBased_afterApplingNewNER_withExactNamesFrom480Hadith.xlsx")

# df2 = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/newNERNamesFrom480Hadith.xlsx")

# hadithNumber = list(df2["HadithNumber"])
# bukhariIndex = []
# for i in range(len(hadithNumber)):
#     bukhariIndex.append(hadithNumber[i])
#     if(i==75):
#         break


# dum = hadithNumber[76:]
# muslimIndex = []
# for i in range(len(dum)):
#     muslimIndex.append(dum[i])
#     if(i==4):
#         break


# dum1 = dum[5:]
# ibnMajaIndex = []
# for i in range(len(dum1)):
#     ibnMajaIndex.append(dum1[i])
#     if(i==77):
#         break


# dum2 = dum1[78:]
# abuDaudIndex = []
# for i in range(len(dum2)):
#     abuDaudIndex.append(dum2[i])
#     if(i==75):
#         break


# dum3 = dum2[76:]
# nesaiIndex = []
# for i in range(len(dum3)):
#     nesaiIndex.append(dum3[i])
#     if(i==76):
#         break


# dum4 = dum3[77:]
# tirmiziIndex = []
# for i in range(len(dum4)):
#     tirmiziIndex.append(dum4[i])
#     if(i==72):
#         break





# dum5 = dum4[73:]
# bukhariIndex1 = []
# for i in range(len(dum5)):
#     bukhariIndex1.append(dum5[i])
#     if(i==11):
#         break


# dum6 = dum5[12:]
# muslimIndex1 = []
# for i in range(len(dum6)):
#     muslimIndex1.append(dum6[i])
#     if(i==11):
#         break


# dum7 = dum6[12:]
# ibnMajaIndex1 = []
# for i in range(len(dum7)):
#     ibnMajaIndex1.append(dum7[i])
#     if(i==11):
#         break


# dum8 = dum7[12:]
# abuDaudIndex1 = []
# for i in range(len(dum8)):
#     abuDaudIndex1.append(dum8[i])
#     if(i==11):
#         break


# dum9 = dum8[12:]
# nesaiIndex1 = []
# for i in range(len(dum9)):
#     nesaiIndex1.append(dum9[i])
#     if(i==11):
#         break


# dum10 = dum9[12:]
# tirmiziIndex1 = []
# for i in range(len(dum10)):
#     tirmiziIndex1.append(dum10[i])
#     if(i==11):
#         break


# dum11 = dum10[12:]


# myDb = mysql.connector.connect(host="localhost",user="root",passwd="fb834946220403",database="sihah_al_sittah")
# myCursor = myDb.cursor()
# #1-Bukhari
# #2-Muslim
# #3-Ibn Maja
# #4-Abu Daud
# #5-Nesai
# #6-Trimizi


# # Query for hadith 
# bukhariStatus = []
# for i in range(len(bukhariIndex)):
#     query = '''select arabic_grade from bukhari_book where table_index='''+str(bukhariIndex[i])+''';'''
#     myCursor.execute(query)
#     result = myCursor.fetchall()
#     bukhariStatus.append(result[0][0])
    
# muslimStatus = []
# for i in range(len(muslimIndex)):
#     query = '''select arabic_grade from muslim_book where table_index='''+str(muslimIndex[i])+''';'''
#     myCursor.execute(query)
#     result = myCursor.fetchall()
#     muslimStatus.append(result[0][0])

# ibnMajaStatus = []
# for i in range(len(ibnMajaIndex)):
#     query = '''select arabic_grade from ibnmaja_book where table_index='''+str(ibnMajaIndex[i])+''';'''
#     myCursor.execute(query)
#     result = myCursor.fetchall()
#     ibnMajaStatus.append(result[0][0])

# abuDaudStatus = []
# for i in range(len(abuDaudIndex)):
#     query = '''select arabic_grade from abudaud_book where table_index='''+str(abuDaudIndex[i])+''';'''
#     myCursor.execute(query)
#     result = myCursor.fetchall()
#     abuDaudStatus.append(result[0][0])

# nesaiStatus = []
# for i in range(len(nesaiIndex)):
#     query = '''select arabic_grade from nesai_book where table_index='''+str(nesaiIndex[i])+''';'''
#     myCursor.execute(query)
#     result = myCursor.fetchall()
#     nesaiStatus.append(result[0][0])

# tirmiziStatus = []
# for i in range(len(tirmiziIndex)):
#     query = '''select arabic_grade from tirmizi_book where table_index='''+str(tirmiziIndex[i])+''';'''
#     myCursor.execute(query)
#     result = myCursor.fetchall()
#     tirmiziStatus.append(result[0][0])




# bukhariStatus1 = []
# for i in range(len(bukhariIndex1)):
#     query = '''select arabic_grade from bukhari_book where table_index='''+str(bukhariIndex1[i])+''';'''
#     myCursor.execute(query)
#     result = myCursor.fetchall()
#     bukhariStatus1.append(result[0][0])

# muslimStatus1 = []
# for i in range(len(muslimIndex1)):
#     query = '''select arabic_grade from muslim_book where table_index='''+str(muslimIndex1[i])+''';'''
#     myCursor.execute(query)
#     result = myCursor.fetchall()
#     muslimStatus1.append(result[0][0])

# ibnMajaStatus1 = []
# for i in range(len(ibnMajaIndex1)):
#     query = '''select arabic_grade from ibnmaja_book where table_index='''+str(ibnMajaIndex1[i])+''';'''
#     myCursor.execute(query)
#     result = myCursor.fetchall()
#     ibnMajaStatus1.append(result[0][0])

# abuDaudStatus1 = []
# for i in range(len(abuDaudIndex1)):
#     query = '''select arabic_grade from abudaud_book where table_index='''+str(abuDaudIndex1[i])+''';'''
#     myCursor.execute(query)
#     result = myCursor.fetchall()
#     abuDaudStatus1.append(result[0][0])

# nesaiStatus1 = []
# for i in range(len(nesaiIndex1)):
#     query = '''select arabic_grade from nesai_book where table_index='''+str(nesaiIndex1[i])+''';'''
#     myCursor.execute(query)
#     result = myCursor.fetchall()
#     nesaiStatus1.append(result[0][0])

# tirmiziStatus1 = []
# for i in range(len(tirmiziIndex1)):
#     query = '''select arabic_grade from tirmizi_book where table_index='''+str(tirmiziIndex1[i])+''';'''
#     myCursor.execute(query)
#     result = myCursor.fetchall()
#     tirmiziStatus1.append(result[0][0])





# allBooksIndex = []

# allBooksStatus = []

# allBooksIndex = bukhariIndex + muslimIndex + ibnMajaIndex + abuDaudIndex + nesaiIndex + tirmiziIndex + bukhariIndex1 + muslimIndex1 + ibnMajaIndex1 + abuDaudIndex1 + nesaiIndex1 + tirmiziIndex1

# allBooksStatus = bukhariStatus + muslimStatus + ibnMajaStatus + abuDaudStatus + nesaiStatus + tirmiziStatus + bukhariStatus1 + muslimStatus1 + ibnMajaStatus1 + abuDaudStatus1 + nesaiStatus1 + tirmiziStatus1

# ahadithText = list(df2["HadithText"])

# ahadithText = ahadithText[:457]

# exactNames = list(df["ExactNames"])

# exactNames = exactNames[:457]

# df3 = pd.DataFrame()

# df3["HadithNumber"] = allBooksIndex

# df3["HadithText"] = ahadithText

# df3["ExactNames"] = exactNames

# df3["Status"] = allBooksStatus

# df3.to_excel("C:/Users/iammu/OneDrive/Desktop/DatasetOf457AhadithForML(old).xlsx")


# statuses = list(df4["Status"])


# count=0
# for i in range(len(statuses)):
#     if(type(statuses[i])==float):
#         continue
#     if(statuses[i].strip()=='حسن'):
#         print(i,end=" ")
#         count+=1
#         # statuses[i] = 'صحيح'

# statuses[193] = 'صحيح'

# statuses[430] = 'ضعيف'

# statuses[425] = 'ضعيف'

# statuses[230]

# statuses[326]

# statuses[361]

# statuses[376]

# df4 = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/SahihAhadith2400.xlsx")

# df4["Status"] = statuses

# df4.to_excel("C:/Users/iammu/OneDrive/Desktop/DatasetOf457AhadithForML.xlsx")

import pandas as pd
import numpy as np
import mysql.connector



dfMatchName = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/MatchNameFromAllTrainTestHadith.xlsx")
dfTrain = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/4000MatchNameWithDataBase.xlsx")
dfTest = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/600MatchNameWithDataBase.xlsx")



exactSingleNames = list(dfMatchName['Match_Name'])
trainMatchList=list(dfTrain.MatchName)
testMatchList = list(dfTest.MatchName)

# eNames = list(df5["ExactNames"])
# eStatus = list(df5["Status"])
finalTrainMatchList = []
for i in range(len(dfTrain)):
    x=dfTrain.MatchName[i]
    x = x.replace('[','')
    x = x.replace(']','')
    x = x.replace("'","")
    
    xList = x.split(",")
    xList = [item.strip() for item in xList]
    finalTrainMatchList.append(xList)
    
finalTestMatchList = []
for i in range(len(dfTest)):
    x=dfTest.MatchName[i]
    x = x.replace('[','')
    x = x.replace(']','')
    x = x.replace("'","")
    
    xList = x.split(",")
    xList = [item.strip() for item in xList]
    finalTestMatchList.append(xList)
    


# narratorNames=[]

# for i in range(len(finalTrainMatchList)):
#     for j in range(len(finalTrainMatchList[i])):
#         narratorNames.append(finalTrainMatchList[i][j])
        
# for i in range(len(finalTestMatchList)):
#     for j in range(len(finalTestMatchList[i])):
#         narratorNames.append(finalTestMatchList[i][j])
        

# narratorNames = list(dict.fromkeys(narratorNames))


exactSingleNames = list(dfMatchName.Match_Name)

exactSingleNames = list(dict.fromkeys(exactSingleNames))


# for i in range(len(narratorNames)):
#     if(narratorNames[i] in exactName):
#         continue
#     else:
#         print(narratorNames[i])

# a=[1,2,3,2,0]

# sparseMatrix = [[0]*1107]*453
# sparseMatrix = np.array(sparseMatrix)



sparseMatrix = np.zeros((4687,3352))
k=0
for i in range(len(sparseMatrix)):
    print(i)
    # dumm = eNames[i]
    # dumm = dumm.replace('[','')
    # dumm = dumm.replace(']','')
    # dumm = dumm.replace("'","")
    
    # dummList = dumm.split(",")
    # dummList = [item.strip() for item in dummList]
    if(i<=4088):
        for j in range(len(exactSingleNames)):
            if(exactSingleNames[j] in finalTrainMatchList[i]):
                sparseMatrix[i][j]=1.0
    else:
        for j in range(len(exactSingleNames)):
            if(exactSingleNames[j] in finalTestMatchList[k]):
                sparseMatrix[i][j]=1.0
        k=k+1


    
y_axis =[]
for i in range(len(dfTrain)):
    if(dfTrain.Status[i]=='صحيح'):
        y_axis.append(1.0)
    else:
        y_axis.append(0.0)
     
for i in range(len(dfTest)):
    if(dfTest.Status[i]=='صحيح'):
        y_axis.append(1.0)
    else:
        y_axis.append(0.0)
     
# Train Test Split
X_train = sparseMatrix[:4187]
Y_train = np.array(y_axis[:4187])
X_test = sparseMatrix[4187:]
Y_test = np.array(y_axis[4187:])


# # Adding input layer and first hidden layer
# classifier.add(Dense(output_dim = 4,  activation = 'relu', input_dim = 3))

# # Adding second hidden layer
# classifier.add(Dense(output_dim = 4,  activation = 'relu’))

# # Adding second out layer
# classifier.add(Dense(output_dim = 1,  activation = ‘sigmoid'))

                     

import tensorflow as tf
from tensorflow import keras

model = keras.models.Sequential()
model.add(keras.layers.Dense(4687, activation="relu", input_shape=X_train.shape[1:]))
model.add(keras.layers.Dense(1500, activation="relu"))
model.add(keras.layers.Dense(1, activation="sigmoid"))

classes=['Daif','Sahih']

model.compile(loss="binary_crossentropy",
 optimizer="adam",
 metrics=["accuracy"])





history = model.fit(X_train, Y_train, epochs=1)
model.evaluate(X_test,Y_test)





prob = model.predict(X_test)
prob.round(2)
model.predict_classes(X_test[:5])

prob_class = []

for i in range(len(prob)):
    if(prob[i][0]>0.5):
        prob_class.append('صحيح')
    else:
        prob_class.append('ضعيف')                     


d1 = FinalStatus_test
# Matching Predicted Results with Actual Testing Results
notMatch = 0
for i in range(len(prob_class)):
    if(prob_class[i]!=d1[i]):
        print(i, end=" ")
        notMatch+=1


accuracy = (len(Y_test)-notMatch)/len(Y_test)




