# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 18:37:53 2022

@author: Ali Baqar
"""
import pandas as pd
df = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/copied fyp/Hadith&FullExactNameOfNarrator.xlsx")

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

