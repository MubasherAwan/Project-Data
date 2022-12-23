# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 11:35:56 2022

@author: iammu
"""
selectedHAdith=[]

import mysql.connector
myDb = mysql.connector.connect(host="localhost",user="root",passwd="fb834946220403",database="sihah_al_sittah")
myCursor = myDb.cursor()

#1-Bukhari
#2-Muslim
#3-Ibn Maja
#4-Abu Daud
#5-Nesai
#6-Trimizi



# Query for hadith 
query = '''select table_index,arabic_hadith from tirmizi_book where table_index>21 and table_index<100;'''
myCursor.execute(query)
result = myCursor.fetchall()
count=0


for i in range(len(result)):
    if(result[i][1].__contains__("تَعَالَى")):
        print("Hadith Qudsiii")
    else:
        selectedHAdith.append(result[i])
        count+=1
    if(count==80):
        break
    
    
import pandas as pd

df = pd.DataFrame()


numberList  =[]
hadithList =[]
for i in range(len(selectedHAdith)):
    numberList.append(selectedHAdith[i][0]) 
    hadithList.append(selectedHAdith[i][1])

df["HadithNumber"] = numberList




HadithList = df.HadithText
WithoutAhrabList=[]
#sentence="وَحَدَّثَنَا مُحَمَّدُ بْنُ عَبْدِ اللَّهِ بْنِ نُمَيْرٍ، حَدَّثَنَا أَبِي، حَدَّثَنَا سَعِيدُ بْنُ عُبَيْدٍ، حَدَّثَنَا عَلِيُّ بْنُ رَبِيعَةَ، قَالَ أَتَيْتُ الْمَسْجِدَ وَالْمُغِيرَةُ أَمِيرُ الْكُوفَةِ قَالَ فَقَالَ الْمُغِيرَةُ سَمِعْتُ رَسُولَ اللَّهِ صلى الله عليه وسلم يَقُولُ ‏ ‏ إِنَّ كَذِبًا عَلَىَّ لَيْسَ كَكَذِبٍ عَلَى أَحَدٍ فَمَنْ كَذَبَ عَلَىَّ مُتَعَمِّدًا فَلْيَتَبَوَّأْ مَقْعَدَهُ مِنَ النَّارِ ‏‏ ‏.‏ ‏"
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


df["HadithText"] = WithoutAhrabList



df.to_excel("500HadithFromDifferentBooks.xlsx")
