# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:10:54 2022

@author: iammu
"""

import mysql.connector
import pandas as pd

# Function for Removing Aeraab from Arabic Text
def aeraabRemover(HadithList):
    WithoutAhrabList=[]
    for hadith in HadithList:
        dum123 = ""
        # Aeraab Remover Code
        for i in range(len(hadith)):
            no = ord(hadith[i])
            if (no == 1614 or no == 1615 or no == 1616 or no == 1618 or no == 1617 or no == 1612 or no == 1613 or no == 1611):
                continue
            else:
                dum123 += hadith[i]

        dum123 = dum123.strip()
        WithoutAhrabList.append(dum123)
    return WithoutAhrabList

myDb = mysql.connector.connect(host="localhost", user="root", passwd="fb834946220403", database="sihah_al_sittah")
myCursor = myDb.cursor()


allBooksIsnads = []
allBooksGrades = []

#1-Bukhari
#2-Muslim
#3-Ibn Maja
#4-Abu Daud
#5-Nesai
#6-Trimizi

query = '''select arabic_isnad,arabic_grade from bukhari_book  where arabic_grade="صحيح" limit 400;'''
myCursor.execute(query)
result = myCursor.fetchall()
for i in range(len(result)):
    allBooksIsnads.append(result[i][0])
    allBooksGrades.append(result[i][1])

query = '''select arabic_isnad,arabic_grade from muslim_book   where arabic_grade="صحيح" limit 400;'''
myCursor.execute(query)
result = myCursor.fetchall()
for i in range(len(result)):
    allBooksIsnads.append(result[i][0])
    allBooksGrades.append(result[i][1])

query = '''select arabic_isnad,arabic_grade from ibnmaja_book   where arabic_grade="صحيح" limit 400;'''
myCursor.execute(query)
result = myCursor.fetchall()
for i in range(len(result)):
    allBooksIsnads.append(result[i][0])
    allBooksGrades.append(result[i][1])

query = '''select arabic_isnad,arabic_grade from abudaud_book   where arabic_grade="صحيح" limit 400;'''
myCursor.execute(query)
result = myCursor.fetchall()
for i in range(len(result)):
    allBooksIsnads.append(result[i][0])
    allBooksGrades.append(result[i][1])

query = '''select arabic_isnad,arabic_grade from nesai_book  where arabic_grade="صحيح" limit 400;'''
myCursor.execute(query)
result = myCursor.fetchall()
for i in range(len(result)):
    allBooksIsnads.append(result[i][0])
    allBooksGrades.append(result[i][1])

query = '''select arabic_isnad,arabic_grade from tirmizi_book  where arabic_grade="صحيح" limit 400;'''
myCursor.execute(query)
result = myCursor.fetchall()
for i in range(len(result)):
    allBooksIsnads.append(result[i][0])
    allBooksGrades.append(result[i][1])


allBooksIsnads = aeraabRemover(allBooksIsnads)

#Only for counting Sahih and Daif
count=0
for i in range(len(allBooksGrades)):
    if(allBooksGrades[i]=='صحيح' or allBooksGrades[i]=='ضعيف'):
        count+=1

#For counting other than Sahih and Daif
count1=0
for i in range(len(allBooksGrades)):
    if(allBooksGrades[i]!='صحيح' and allBooksGrades[i]!='ضعيف'):
        count1+=1

#For printing index other than Sahih and Daif
# for i in range(len(allBooksGrades)):
#     if(allBooksGrades[i]!='صحيح' and allBooksGrades[i]!='ضعيف'):
#         print(i,end=" ")

#For printing grade other than Sahih and Daif
# for i in range(len(allBooksGrades)):
#     if(allBooksGrades[i]!='صحيح' and allBooksGrades[i]!='ضعيف'):
#         print(allBooksGrades[i],end=" ,")

#For changing grade from Hassan to Sahih
for i in range(len(allBooksGrades)):
    if(allBooksGrades[i]=='حسن'):
        allBooksGrades[i] = 'صحيح'

#For changing grade from Hassan Sahih to Sahih
for i in range(len(allBooksGrades)):
    if(allBooksGrades[i]=='حسن صحيح'):
        allBooksGrades[i] = 'صحيح'
        
#For changing grade from Shaaz to Sahih
for i in range(len(allBooksGrades)):
    if(allBooksGrades[i]=='شاذ'):
        allBooksGrades[i] = 'ضعيف'
        
#For changing grade from Munkar to Sahih
for i in range(len(allBooksGrades)):
    if(allBooksGrades[i]=='منكر'):
        allBooksGrades[i] = 'ضعيف'

#For changing grade from Sahih_al_isnad to Sahih
for i in range(len(allBooksGrades)):
    if(allBooksGrades[i]=='صحيح الإسناد'):
        allBooksGrades[i] = 'صحيح'
        
#For changing grade from Sahih_al_isnad to Sahih
for i in range(len(allBooksGrades)):
    if(allBooksGrades[i]=='صحيح موقوف'):
        allBooksGrades[i] = 'صحيح'
        



# count=0
# for i in range(len(allBooksGrades)):
#     if(allBooksGrades[i]!='صحيح' and allBooksGrades[i]!='ضعيف'):
#         # allBooksGrades[i] = 'صحيح'
#         count+=1
#         # print(i,end=" ")

# allBooksGrades[195] = 'صحيح'
# allBooksGrades[285]



df6 = pd.DataFrame()
df6["isnad"] = allBooksIsnads
df6["status"] = allBooksGrades

counter=0
for i in range(len(allBooksGrades)):
    if((allBooksGrades[i])==" "):
        counter=counter+1
        df6.drop(i,axis=0,inplace=True)
        print(i,end=(" ,"))

df6.to_excel("C:/Users/iammu/OneDrive/Desktop/SahihAhadith2400.xlsx")


