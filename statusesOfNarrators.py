# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:52:38 2022

@author: Ali Baqar
"""
import mysql.connector

import pandas as pd

# Loading excel file
df = pd.read_excel("C:/Users/Ali Baqar/Desktop/PythonCodes/NarratorStatusList.xlsx")
# Saving excel file as a list in a variable
narratorsStatusList = list(df.Status)
# Loading excel file
df1 = pd.read_excel("C:/Users/Ali Baqar/Desktop/PythonCodes/distinctAreaOfIntrest.xlsx")
# Saving excel file as a list in a variable
narratorsAreaOfIntrest = list(df1.area_of_intrest)


# For changing type from float to string
for i in range(len(narratorsAreaOfIntrest)):
    if(type(narratorsAreaOfIntrest[i])==float):
        narratorsAreaOfIntrest[i] = str(narratorsAreaOfIntrest[i])
        
        
        

# List that contains ids of scholars according to their Area of Intrest
narratorsIdAccToAreaOfIntrest = []
# Connection with scholar_intrests DataBase
myDb = mysql.connector.connect(host="localhost", user="root", passwd="Alibaqar_98680", database="scholar_intrests")

myCursor = myDb.cursor()
# Extracting ids from DataBase According to Area of Intrest of Scholars
for i in range(len(narratorsAreaOfIntrest)):
    
    narratorsId = []
    
    query = "select scholar_id from area_of_intrest where name = '"+narratorsAreaOfIntrest[i]+"';"
    
    myCursor.execute(query)
    
    result = myCursor.fetchall()
    
    for j in range(len(result)):
        narratorsId.append(result[j][0])
    
    narratorsIdAccToAreaOfIntrest.append(narratorsId)

myDb.commit()
myCursor.close()
myDb.close()




# Connection with dummy DataBase
myDb1 = mysql.connector.connect(host="localhost", user="root", passwd="Alibaqar_98680", database="dummy")

myCursor1 = myDb1.cursor()

# scholarIdsList = []

# query1 = "select id from scholars;"

# myCursor1.execute(query1)

# result1 = myCursor1.fetchall()

# for i in range(len(result1)):
    # scholarIdsList.append(result1[i][0])

# narratorsJarahTaadeelList = []

for i in range(len(narratorsStatusList)):
        indexList = narratorsIdAccToAreaOfIntrest[i]
        for j in range(len(indexList)):
            query1 = "update scholars set Jarah_Taadeel='"+narratorsStatusList[i]+"' where id="+str(indexList[j])+";"
            
            myCursor1.execute(query1)
            
            myDb1.commit()
            

query1 = "select status from scholars where Jarah_Taadeel='nan';"
myCursor1.execute(query1)
result = myCursor1.fetchall() 

nanScholarIds = []
nanScholarsName = []
nanScholarsStatus = []

for i in range(len(result)):
    nanScholarsStatus.append(result[i][0])

myCursor1.close()
myDb1.close()

df2 = pd.DataFrame(columns=["id","name","status"])
df2["id"] = nanScholarIds
df2["name"] = nanScholarsName 
df2["status"] = nanScholarsStatus

df2.to_excel("nanScholarsInfo.xlsx")


for i in range(len(nanScholarIds)):
    query1 = "update scholars set Jarah_Taadeel='Zaeef' where id="+str(nanScholarIds[i])+";"
    
    myCursor1.execute(query1)
    
    myDb1.commit()


myDb1.commit()
myCursor1.close()
myDb1.close()

# Connection with dummy DataBase
myDb1 = mysql.connector.connect(host="localhost", user="root", passwd="Alibaqar_98680", database="dummy")

myCursor1 = myDb1.cursor()

query1 = "select Jarah_Taadeel from scholars;"
myCursor1.execute(query1)
result = myCursor1.fetchall() 

dummyScholarsId = []
dummyScholarsJarahTaadeel = []

for i in range(len(result)):
    dummyScholarsJarahTaadeel.append(result[i][0])
    


# Connection with scholar_database DataBase
myDb1 = mysql.connector.connect(host="localhost", user="root", passwd="Alibaqar_98680", database="scholar_database")

myCursor1 = myDb1.cursor()    
for i in range(len(dummyScholarsId)):
    query1 = "update scholars set Jarah_Taadeel='"+dummyScholarsJarahTaadeel[i]+"' where id="+str(dummyScholarsId[i])+";"
    
    myCursor1.execute(query1)
    
    myDb1.commit()

myDb1.commit()
myCursor1.close()
myDb1.close()





