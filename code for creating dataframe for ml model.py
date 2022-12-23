# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 11:56:29 2022

@author: iammu
"""

import mysql.connector

myDb = mysql.connector.connect(host="localhost", user="root", passwd="fb834946220403", database="sihah_al_sittah")
myCursor = myDb.cursor()

isnadTrainingList = []

gradeTrainingList = []

query1 = "select arabic_hadith,arabic_grade from bukhari_book where arabic_grade='صحيح';"
myCursor.execute(query1)
result1 = myCursor.fetchall()

print(len(result1))
for i in range(len(result1)):
    isnadTrainingList.append(result1[i][0])
    gradeTrainingList.append(result1[i][1])

query2 = "select arabic_hadith,arabic_grade from muslim_book where arabic_grade='صحيح';"
myCursor.execute(query2)
result2 = myCursor.fetchall()

print(len(result2))
for i in range(len(result2)):
    isnadTrainingList.append(result2[i][0])
    gradeTrainingList.append(result2[i][1])
    

query3 = "select arabic_hadith,arabic_grade from ibnMaja_book where arabic_grade='صحيح';"
myCursor.execute(query3)
result3 = myCursor.fetchall()

print(len(result3))
for i in range(len(result3)):
    isnadTrainingList.append(result3[i][0])
    gradeTrainingList.append(result3[i][1])



query4 = "select arabic_hadith,arabic_grade from ibnMaja_book where arabic_grade='حسن';"
myCursor.execute(query4)
result4 = myCursor.fetchall()

print(len(result4))
for i in range(len(result4)):
    isnadTrainingList.append(result4[i][0])
    gradeTrainingList.append(result4[i][1])



query5 = "select arabic_hadith,arabic_grade from ibnMaja_book where arabic_grade='ضعيف';"
myCursor.execute(query5)
result5 = myCursor.fetchall()

print(len(result5))
for i in range(len(result5)):
    isnadTrainingList.append(result5[i][0])
    gradeTrainingList.append(result5[i][1])



query6 = "select arabic_hadith,arabic_grade from tirmizi_book where arabic_grade='صحيح';"
myCursor.execute(query6)
result6 = myCursor.fetchall()

print(len(result6))
for i in range(len(result6)):
    isnadTrainingList.append(result6[i][0])
    gradeTrainingList.append(result6[i][1])



query7 = "select arabic_hadith,arabic_grade from tirmizi_book where arabic_grade='حسن';"
myCursor.execute(query7)
result7 = myCursor.fetchall()

print(len(result7))
for i in range(len(result7)):
    isnadTrainingList.append(result7[i][0])
    gradeTrainingList.append(result7[i][1])



query8 = "select arabic_hadith,arabic_grade from tirmizi_book where arabic_grade='ضعيف';"
myCursor.execute(query8)
result8 = myCursor.fetchall()

print(len(result8))
for i in range(len(result8)):
    isnadTrainingList.append(result8[i][0])
    gradeTrainingList.append(result8[i][1])



query9 = "select arabic_hadith,arabic_grade from abuDaud_book where arabic_grade='صحيح';"
myCursor.execute(query9)
result9 = myCursor.fetchall()

print(len(result9))
for i in range(len(result9)):
    isnadTrainingList.append(result9[i][0])
    gradeTrainingList.append(result9[i][1])



query10 = "select arabic_hadith,arabic_grade from abuDaud_book where arabic_grade='صحيح موقوف';"
myCursor.execute(query10)
result10 = myCursor.fetchall()

print(len(result10))
for i in range(len(result10)):
    isnadTrainingList.append(result10[i][0])
    gradeTrainingList.append('صحيح')



query11 = "select arabic_hadith,arabic_grade from abuDaud_book where arabic_grade='صحيح مقطوع';"
myCursor.execute(query11)
result11 = myCursor.fetchall()

print(len(result11))
for i in range(len(result11)):
    isnadTrainingList.append(result11[i][0])
    gradeTrainingList.append('صحيح')



query12 = "select arabic_hadith,arabic_grade from abuDaud_book where arabic_grade='حسن';"
myCursor.execute(query12)
result12 = myCursor.fetchall()

print(len(result12))
for i in range(len(result12)):
    isnadTrainingList.append(result12[i][0])
    gradeTrainingList.append(result12[i][1])



query13 = "select arabic_hadith,arabic_grade from abuDaud_book where arabic_grade='ضعيف';"
myCursor.execute(query13)
result13 = myCursor.fetchall()

print(len(result13))
for i in range(len(result13)):
    isnadTrainingList.append(result13[i][0])
    gradeTrainingList.append(result13[i][1])



query14 = "select arabic_hadith,arabic_grade from abuDaud_book where arabic_grade='شاذ';"
myCursor.execute(query14)
result14 = myCursor.fetchall()

print(len(result14))
for i in range(len(result14)):
    isnadTrainingList.append(result14[i][0])
    gradeTrainingList.append('ضعيف')



query15 = "select arabic_hadith,arabic_grade from abuDaud_book where arabic_grade='منكر';"
myCursor.execute(query15)
result15 = myCursor.fetchall()

print(len(result15))
for i in range(len(result15)):
    isnadTrainingList.append(result15[i][0])
    gradeTrainingList.append('ضعيف')



query16 = "select arabic_hadith,arabic_grade from nesai_book where arabic_grade='صحيح';"
myCursor.execute(query16)
result16 = myCursor.fetchall()

print(len(result16))
for i in range(len(result16)):
    isnadTrainingList.append(result16[i][0])
    gradeTrainingList.append(result16[i][1])



query17 = "select arabic_hadith,arabic_grade from nesai_book where arabic_grade='حسن';"
myCursor.execute(query17)
result17 = myCursor.fetchall()

print(len(result17))
for i in range(len(result17)):
    isnadTrainingList.append(result17[i][0])
    gradeTrainingList.append(result17[i][1])



query18 = "select arabic_hadith,arabic_grade from nesai_book where arabic_grade='ضعيف';"
myCursor.execute(query18)
result18 = myCursor.fetchall()

print(len(result18))
for i in range(len(result18)):
    isnadTrainingList.append(result18[i][0])
    gradeTrainingList.append(result18[i][1])

import pandas as pd
df1 = pd.DataFrame()
df1["arabic_hadith"] = isnadTrainingList
df1["arabic_grade"] = gradeTrainingList

df1.to_csv("C:/Users/iammu/OneDrive/Desktop/DataForMachineLearningV1.csv")
