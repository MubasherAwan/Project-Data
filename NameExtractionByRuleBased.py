# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 12:15:36 2022

@author: iammu
"""



import mysql.connector
myDb = mysql.connector.connect(host="localhost",user="root",passwd="fb834946220403",database="sihah_al_sittah")
myCursor = myDb.cursor()


# Query for hadith 
query = '''select table_index,arabic_hadith from nesai_book where table_index<=10;'''
myCursor.execute(query)
result = myCursor.fetchall()


NameFromRuleBase=[]
for res in result:
#     getHadithText='''أَخْبَرَنَا عَمْرُو بْنُ عَلِيٍّ، حَدَّثَنَا يَحْيَى، - وَهُوَ ابْنُ سَعِيدٍ - قَالَ حَدَّثَنَا قُرَّةُ بْنُ خَالِدٍ، قَالَ حَدَّثَنَا حُمَيْدُ بْنُ هِلاَلٍ، قَالَ حَدَّثَنِي أَبُو بُرْدَةَ، عَنْ أَبِي مُوسَى، قَالَ أَقْبَلْتُ إِلَى النَّبِيِّ صلى الله عليه وسلم وَمَعِي رَجُلاَنِ مِنَ الأَشْعَرِيِّينَ أَحَدُهُمَا عَنْ يَمِينِي وَالآخَرُ عَنْ يَسَارِي وَرَسُولُ اللَّهِ صلى الله عليه وسلم يَسْتَاكُ فَكِلاَهُمَا سَأَلَ الْعَمَلَ قُلْتُ وَالَّذِي بَعَثَكَ بِالْحَقِّ نَبِيًّا مَا أَطْلَعَانِي عَلَى مَا فِي أَنْفُسِهِمَا وَمَا شَعَرْتُ أَنَّهُمَا يَطْلُبَانِ الْعَمَلَ فَكَأَنِّي أَنْظُرُ إِلَى سِوَاكِهِ تَحْتَ شَفَتِهِ قَلَصَتْ فَقَالَ ‏ ‏ إِنَّا لاَ - أَوْ لَنْ - نَسْتَعِينَ عَلَى الْعَمَلِ مَنْ أَرَادَهُ وَلَكِنِ اذْهَبْ أَنْتَ ‏‏ ‏.‏ فَبَعَثَهُ عَلَى الْيَمَنِ ثُمَّ أَرْدَفَهُ مُعَاذُ بْنُ جَبَلٍ رضى الله عنهما ‏.‏'''

    # Removing before and after white spaces
    hadithText = result[res][1].strip()

    # Variable that contains without_Aeraab hadithText
    withoutAerabText = ""

    # Aeraab Remover Code
    for i in range(len(hadithText)):
        no = ord(hadithText[i])
        if (no == 1614 or no == 1615 or no == 1616 or no == 1618 or no == 1617 or no == 1612 or no == 1613 or no == 1611):
            continue
        else:
            withoutAerabText += hadithText[i]

    # Split hadithText into words on the basis of space and create a list
    tokens_WithoutAerabText = withoutAerabText.split(" ")

    # Words that replace from hadithText
    WordReplace = ["حدثني", "في" , "أنها" , "وحدثنا", "حدثنا", "أنبأنا","ـ", "نحوه", "عن", "قال", "فقال", "سمعت", "يقول", "أنه", "سمع", "أخبرني",
                           "مولى", "أخبرنا", "اخبرنا", "سال", "أن", "قالت", ":", "في حديثه", "تابعه", "أخبره", "ان", "انه",
                           "اخبرني", "وحدثني", "وأخبرني"]


    # Extract all words from hadithText Like "حدثني","وحدثنا","حدثنا"
    wordReplaceList_givenHadith = []

    # Extract all Narrator's Names from given hadith
    narratorsNameList = []

    # Variable for extracting WordReplace's element from hadithText  Like "حدثني","وحدثنا","حدثنا"
    get_WordReplace_Element = ""

    # Variable for extracting Name of Narrator from hadithText and at the end Matn of hadith
    narratorName = ""

    for i in range(len(tokens_WithoutAerabText)):

        if (tokens_WithoutAerabText[i] in WordReplace) == True:
            get_WordReplace_Element += (tokens_WithoutAerabText[i] + " ")
            if (narratorName != ""):
                narratorsNameList.append(narratorName)
                narratorName = ""
        if (tokens_WithoutAerabText[i] in WordReplace) == False:
            narratorName += (tokens_WithoutAerabText[i] + " ")
            if (get_WordReplace_Element != ""):
                wordReplaceList_givenHadith.append(get_WordReplace_Element)
                get_WordReplace_Element = ""


    # List of Prophet's صلی اللہ علیہ وآلہ وسلم name that are used in Ahadith
    prophetNamesReplacerList = ["رسول الله صلى الله عليه وسلم","النبي ـ صلى الله عليه وسلم" ,"النبي صلى الله عليه وسلم", "يا رسول الله",
                                        "محمد صلی اللہ علیہ وآلہ وسلم"]


    # Script for Qauli and Faeli Hadith in which Prophet's(صلی اللہ علیہ وآلہ وسلم) name used in Matn only
    for i in range(len(prophetNamesReplacerList)):
        if (prophetNamesReplacerList[i] not in narratorsNameList and narratorName.__contains__(prophetNamesReplacerList[i])):
            narratorsNameList.append("محمد صلی اللہ علیہ وآلہ وسلم")

    # Script also used for same work as mentioned in above comment
    for i in range(len(narratorsNameList)):
        for j in range(len(prophetNamesReplacerList)):
            if (narratorsNameList[i].__contains__(prophetNamesReplacerList[j]) and narratorsNameList[i] !=prophetNamesReplacerList[j]):
                narratorsNameList[i] = "محمد صلی اللہ علیہ وآلہ وسلم"

    for i in range(len(prophetNamesReplacerList)):
        if(withoutAerabText.__contains__(prophetNamesReplacerList[i])):
            narratorsNameList.append("محمد صلی اللہ علیہ وآلہ وسلم")
    # Removing duplicate values
    narratorsNameList = list(dict.fromkeys(narratorsNameList))


    #   ****************New Search Algorithm asked by Sir****************

    # narratorsNameList[0] = "الحميدي عبد الله بن أبي الزبير"
    # Filtering Names of narrators
    for i in range(len(narratorsNameList)):
        narratorsNameList[i] = narratorsNameList[i].strip()
        if (len(narratorsNameList[i]) != 0):
            if (narratorsNameList[i][-1] == "،"):
                narratorsNameList[i] = narratorsNameList[i].replace("،", "")

        narratorsNameList[i] = narratorsNameList[i].replace('''"''', '')
        narratorsNameList[i] = narratorsNameList[i].replace("ـ رضى الله عنها ـ", "")
        narratorsNameList[i] = narratorsNameList[i].replace("ـ رضى الله عنهما ـ", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضي الله عنها", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضي الله عنه", "")
        narratorsNameList[i] = narratorsNameList[i].replace("على المنبر", "")
        narratorsNameList[i] = narratorsNameList[i].strip()

    refinedNarratorNamesList= []
    for i in range(len(narratorsNameList)):
        if(narratorsNameList[i]!="محمد صلی اللہ علیہ وآلہ وسلم"):
            refinedNarratorNamesList.append(narratorsNameList[i])
        else:
            refinedNarratorNamesList.append(narratorsNameList[i])
            break

    for i in range(len(refinedNarratorNamesList)):
        if(refinedNarratorNamesList[i].__contains__("-")):
            firstDash=refinedNarratorNamesList[i].index('-')
            lastDash= refinedNarratorNamesList[i].rfind('-')

            nameCut = refinedNarratorNamesList[i][firstDash+1:lastDash]
            
    NameFromRuleBase.append(refinedNarratorNamesList)
        
        

