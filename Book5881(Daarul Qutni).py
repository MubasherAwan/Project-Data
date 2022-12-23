# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:53:58 2022

@author: iammu
"""

import pandas as pd

# textFile = open("C:/Users/iammu/OneDrive/Desktop/Text(Siqaat).txt","r",encoding='utf-8')

# textFileData = textFile.read()
# textFileLinesList=textFileData.split("\n")
# refinedTextFileLinesList=[]
# for i in range(len(textFileLinesList)):
#     if(len(textFileLinesList[i].split())==0 or len(textFileLinesList[i].split())==1):
#         continue
#     else:
#         refinedTextFileLinesList.append(textFileLinesList[i])
df=pd.read_excel("C:/Users/iammu/Book_5881.xlsx")


bookDataList=list(df['book5581'])
refinedBookDataList=[]
for i in range(len(bookDataList)):
    if(len(bookDataList[i].split())==0 or len(bookDataList[i].split())==1):
        continue
    else:
        refinedBookDataList.append(bookDataList[i])

narratorIdList=[]
narratorNameList=[]

for i in range(len(refinedBookDataList)):
    if(refinedBookDataList[i][0]=="-"):
        continue
    elif(refinedBookDataList[i].__contains__("-")):
        dum=refinedBookDataList[i].split("-")
        narratorIdList.append(dum[0])
        narratorNameList.append(dum[1])
        
        
data=pd.DataFrame()
data["narrator_Id"]=narratorIdList
data["narrator_Name"]=narratorNameList     



data.to_excel("Info-Extract-Book5881.xlsx")

    