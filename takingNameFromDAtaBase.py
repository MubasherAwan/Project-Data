# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 11:09:15 2022

@author: iammu
"""

import mysql.connector

myDb = mysql.connector.connect(host="localhost",user="root",passwd="fb834946220403",database="dummy")
myCursor = myDb.cursor()


#____Fetch Name from Scholar Table
query = "select id,name from scholars;"

myCursor.execute(query)

result = myCursor.fetchall()
nameList=[]
for i in result:
    nameList.append(i)
    
#____fetch name from Other Scholar Names
query="select scholar_Id,name from scholar_other_names;"
myCursor.execute(query)

results=myCursor.fetchall()

for i in results:
    nameList.append(i)
    


#converting tuple into list
for i in range(len(nameList)):
    nameList[i]=list(nameList[i])


onlyNameFromDatabse = []

for i in range(len(nameList)):
    onlyNameFromDatabse.append(nameList[i][1])

#_____________________________________________________________________________

#____________Name Check In Dataase is Present or not____
import pandas as pd

df = pd.read_csv("C:/Users/iammu/BAG_Of_Name.csv",encoding="utf-8")
bagOfName = list(df.Names)

isPresent = []
notPresent = []


for i in range(len(bagOfName)):
    #bagOfName[i] = bagOfName[i].strip()
    
    if(bagOfName[i] in onlyNameFromDatabse):
        isPresent.append(bagOfName[i])
    else:
        notPresent.append(bagOfName[i])



#Singlr name is preent i Database ___(List onlyNmaeFromDAtabase is retrive from Data base)
("حسان بن عبد الله" in onlyNameFromDatabse)
    

#identifying first "wooo"
woooList=[]
woooIndex=[]
for i in range(len(notPresent)):
    if(notPresent[i][0]=='و'):
        woooIndex.append(i)
        woooList.append(notPresent[i])

#Removing wooo From First Index and then check
        
for i in range(len(woooList)):
    dum=woooList[i]
    dum=dum[1:]
    
    woooList[i]=dum
    
        
#Check with Database words
notPresent_wooo = []
isPresent_wooo = []

Present_woooIndex = []

for i in range(len(woooList)):
    #bagOfName[i] = bagOfName[i].strip()
    
    if(woooList[i] in onlyNameFromDatabse):
        isPresent_wooo.append(woooList[i])
        Present_woooIndex.append(i)
    
    else:
        notPresent_wooo.append(woooList[i])
        
#Removing WOO Staring Word that are present n Database
for i in (Present_woooIndex):
      del notPresent[i]



#Idenfith )








