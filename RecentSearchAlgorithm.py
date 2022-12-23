# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 18:01:09 2022

@author: Ali Baqar
"""

import mysql.connector


# Getting hadith text
getHadithText = '''حَدَّثَنَا الْحُمَيْدِيُّ عَبْدُ اللَّهِ بْنُ الزُّبَيْرِ ، قَالَ : حَدَّثَنَا سُفْيَانُ ، قَالَ : حَدَّثَنَا يَحْيَى بْنُ سَعِيدٍ الْأَنْصَارِيُّ ، قَالَ : أَخْبَرَنِي مُحَمَّدُ بْنُ إِبْرَاهِيمَ التَّيْمِيُّ ، أَنَّهُ سَمِعَ عَلْقَمَةَ بْنَ وَقَّاصٍ اللَّيْثِيَّ ، يَقُولُ : سَمِعْتُ عُمَرَ بْنَ الْخَطَّابِ رَضِيَ اللَّهُ عَنْهُ عَلَى الْمِنْبَرِ، قَالَ : سَمِعْتُ رَسُولَ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ، يَقُولُ : " إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ، وَإِنَّمَا لِكُلِّ امْرِئٍ مَا نَوَى، فَمَنْ كَانَتْ هِجْرَتُهُ إِلَى دُنْيَا يُصِيبُهَا أَوْ إِلَى امْرَأَةٍ يَنْكِحُهَا، فَهِجْرَتُهُ إِلَى مَا هَاجَرَ إِلَيْهِ "'''

# Removing before and after white spaces
hadithText = getHadithText.strip()

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




for i in range(len(narratorsNameList)):
    if(i==0):
        tokens_narratorName = narratorsNameList[i].split(" ")
        
        for j in range(len(tokens_narratorName)):
            # Database Connectivity
            myDb = mysql.connector.connect(host="localhost",user="root",passwd="fb834946220403",database="scholar_database")
            myCursor = myDb.cursor()
            
            query = '''select * from scholars where name like "''' + tokens_narratorName[i] + '''%";'''
            myCursor.execute(query)
            result = myCursor.fetchall()








#   *******************************************************************


# List of all Narrator's Info of given hadith that are present in our DataBase
finalInfoList_Narrators = []


# Cross Check of Narrators_Names with Database
for i in range(len(narratorsNameList)):
    # Database Connectivity
    myDb = mysql.connector.connect(host="localhost",user="root",passwd="fb834946220403",database="scholar_database")
    myCursor = myDb.cursor()
    # add
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


    # Query for checking Narrator's Info in scholars table
    query = '''select * from scholars where name like "''' + narratorsNameList[i] + '''";'''
    myCursor.execute(query)
    result = myCursor.fetchall()
    # Check if Narrator's Info found in scholars table
    if (len(result) != 0):
        finalInfoList_Narrators.append(result[0])
    # Check if Narrator's Info not found in scholars table
    if (len(result) == 0):
        # Query for checking Narrator's Info in scholar_other_names table
        query = '''select * from scholar_other_names
                  where name like "''' + narratorsNameList[i] + '''";'''
        myCursor.execute(query)
        result = myCursor.fetchall()
        # Check if Narrator's Info found in scholar_other_names table
        if (len(result) != 0):
            finalInfoList_Narrators.append(result[0])
        else:
            notFoundNarrators = "Some narrators Not Found in our database"


# Dummy List that contains Refined narratorsNameList i.e. Removing empty cells/values
dummyNarratorsNameList = []


# Code for Removing Empty values from narratorsNameList
for i in range(len(narratorsNameList)):
    if (len(narratorsNameList[i].strip()) != 0):
        dummyNarratorsNameList.append(narratorsNameList[i])

# Assigning dummyNarratorsNameList back to narratorsNameList
narratorsNameList = dummyNarratorsNameList

# List of all Narrator's Ids of given hadith that are present in our DataBase
finalIdList_Narrators = []


# Code for Extracting all Narrator's Ids of Given Hadith and storing in finalIdList_Narrators List
for j in range(len(finalInfoList_Narrators)):
    # Check if Narrator's Info is found from scholars table
    if (len(finalInfoList_Narrators[j]) == 8):
        finalIdList_Narrators.append(finalInfoList_Narrators[j][0])
        continue
    # Check if Narrator's Info is found from scholar_other_names table
    if (len(finalInfoList_Narrators[j]) == 3):
        finalIdList_Narrators.append(finalInfoList_Narrators[j][1])
        continue

# List that contains dictionary of scholar_ids and scholar_names used/present in our given hadith and DataBase also
checkList = []

# Code for combining Scholar_Ids and Scholar_Names in a Dictionary and storing this dictionary in checkList
for i in range(len(finalInfoList_Narrators)):
    if (len(finalInfoList_Narrators[i]) == 8):
        dum = finalInfoList_Narrators[i][0]
        dum1 = finalInfoList_Narrators[i][1]
        dumDict = {'id': dum, 'name': dum1}
        checkList.append(dumDict)
        dum1 = ''
        dum = ''
        dumDict = {}

    if (len(finalInfoList_Narrators[i]) == 3):
        dum = finalInfoList_Narrators[i][1]
        dum1 = finalInfoList_Narrators[i][2]
        dumDict = {'id': dum, 'name': dum1}
        checkList.append(dumDict)
        dum1 = ''
        dum = ''
        dumDict = {}

# List that contains Status_of_Narrators of Given Hadith
statusList = []


# Code for Extracting Status_of_Narrators from Database using Scholar_Ids and storing in statusList
for i in range(len(finalIdList_Narrators)):
    query = "select status from scholars where id = " + str(finalIdList_Narrators[i]) + ";"

    myCursor.execute(query)

    result = myCursor.fetchall()

    for j in range(len(result)):
        statusList.append(result[j][0])

# List that contains dictionary at each index in which we categorized Scholars According to their status
sanadOrder = []



sanadOrder.append({'key': 1, 'status': 'Rasool Allah'})

sanadOrder.append({'key': 2, 'status': 'Comp.(RA)'})
sanadOrder.append({'key': 2, 'status': 'Comp.(RA) [1st Generation]'})
sanadOrder.append({'key': 2, 'status': 'Comp.(RA) [2nd Generation]'})
sanadOrder.append({'key': 2, 'status': 'Comp.(RA) [3rd Generation]'})
sanadOrder.append({'key': 2, 'status': 'Comp.(RA) [4th generation]'})
sanadOrder.append({'key': 2, 'status': 'Comp.(RA) [6th generation]'})
sanadOrder.append({'key': 2, 'status': 'Comp.(RA) [7th generation]'})

sanadOrder.append({'key': 3, 'status': "Follower(Tabi')"})
sanadOrder.append({'key': 3, 'status': "Follower(Tabi') [1st Generation]"})
sanadOrder.append({'key': 3, 'status': "Follower(Tabi') [2nd Generation]"})
sanadOrder.append({'key': 3, 'status': "Follower(Tabi') [3rd Generation]"})
sanadOrder.append({'key': 3, 'status': "Follower(Tabi') [4th generation]"})
sanadOrder.append({'key': 3, 'status': "Follower(Tabi') [5th generation]"})
sanadOrder.append({'key': 3, 'status': "Follower(Tabi') [6th generation]"})
sanadOrder.append({'key': 3, 'status': "Follower(Tabi') [7th generation]"})
sanadOrder.append({'key': 3, 'status': "Follower(Tabi') [8th generation]"})
sanadOrder.append({'key': 3, 'status': "Follower(Tabi') [9th generation]"})
sanadOrder.append({'key': 3, 'status': "Follower(Tabi') [11th generation]"})

sanadOrder.append({'key': 4, 'status': "Succ. (Taba' Tabi')"})
sanadOrder.append({'key': 4, 'status': "Succ. (Taba' Tabi') [7th generation] [Maliki]"})
sanadOrder.append({'key': 4, 'status': "Succ. (Taba' Tabi') [9th generation] [Shafi'ee]"})
sanadOrder.append({'key': 4, 'status': "Succ. (Taba' Tabi') [Hanafi]"})
sanadOrder.append({'key': 4, 'status': "Succ. (Taba' Tabi') [8th generation]"})
sanadOrder.append({'key': 4, 'status': "Succ. (Taba' Tabi') [7th generation]"})
sanadOrder.append({'key': 4, 'status': "Succ. (Taba' Tabi') [6th generation]"})
sanadOrder.append({'key': 4, 'status': "Succ. (Taba' Tabi') [9th generation]"})
sanadOrder.append({'key': 4, 'status': "Succ. (Taba' Tabi') [10th generation]"})
sanadOrder.append({'key': 4, 'status': "Succ. (Taba' Tabi') [9th generation] [Other]"})

sanadOrder.append({'key': 5, 'status': "3rd Century AH"})
sanadOrder.append({'key': 5, 'status': "3rd Century AH [11th generation] [Shafi'ee]"})
sanadOrder.append({'key': 5, 'status': "3rd Century AH [11th generation] [Hanafi]"})
sanadOrder.append({'key': 5, 'status': "3rd Century AH [Shafi'ee]"})
sanadOrder.append({'key': 5, 'status': "3rd Century AH [12th generation]"})
sanadOrder.append({'key': 5, 'status': "3rd Century AH [10th generation] [Hanbali]"})
sanadOrder.append({'key': 5, 'status': "3rd Century AH [10th generation]"})
sanadOrder.append({'key': 5, 'status': "3rd Century AH [11th generation]"})
sanadOrder.append({'key': 5, 'status': "3rd Century AH [10th generation] [Hanafi]"})

sanadOrder.append({'key': 6, 'status': "4th Century AH"})
sanadOrder.append({'key': 6, 'status': "4th Century AH [Other]"})
sanadOrder.append({'key': 6, 'status': "4th Century AH [Shafi'ee]"})
sanadOrder.append({'key': 6, 'status': "4th Century AH [Hanbali]"})

sanadOrder.append({'key': 7, 'status': "5th Century AH"})
sanadOrder.append({'key': 7, 'status': "5th Century AH [Other]"})
sanadOrder.append({'key': 7, 'status': "5th Century AH [Hanbali]"})

sanadOrder.append({'key': 8, 'status': "6th Century AH"})
sanadOrder.append({'key': 8, 'status': "6th Century AH [Hanbali]"})
sanadOrder.append({'key': 8, 'status': "6th Century AH [Maliki]"})
sanadOrder.append({'key': 8, 'status': "6th Century AH [Shafi'ee]"})

sanadOrder.append({'key': 9, 'status': "7th Century AH"})
sanadOrder.append({'key': 9, 'status': "7th Century AH [Shafi'ee]"})
sanadOrder.append({'key': 9, 'status': "7th Century AH [Hanbali]"})

sanadOrder.append({'key': 10, 'status': "8th Century AH"})
sanadOrder.append({'key': 10, 'status': "8th Century AH [Hanbali]"})
sanadOrder.append({'key': 10, 'status': "8th Century AH [Shafi'ee]"})

sanadOrder.append({'key': 11, 'status': "9th Century AH"})
sanadOrder.append({'key': 11, 'status': "9th Century AH [Shafi'ee]"})
sanadOrder.append({'key': 11, 'status': "9th Century AH [Hanbali]"})

sanadOrder.append({'key': 12, 'status': "10th Century AH"})
sanadOrder.append({'key': 12, 'status': "10th Century AH [Hanbali]"})

sanadOrder.append({'key': 13, 'status': "11th Century AH"})
sanadOrder.append({'key': 13, 'status': "11th Century AH [Hanbali]"})

sanadOrder.append({'key': 14, 'status': "12th Century AH"})
sanadOrder.append({'key': 14, 'status': "12th Century AH [Hanbali]"})

sanadOrder.append({'key': 15, 'status': "13th Century AH"})
sanadOrder.append({'key': 15, 'status': "13th Century AH [Hanbali]"})

sanadOrder.append({'key': 16, 'status': "14th Century AH"})
sanadOrder.append({'key': 16, 'status': "14th Century AH [Hanbali]"})

sanadOrder.append({'key': 17, 'status': "15th Century AH"})
sanadOrder.append({'key': 17, 'status': "15th Century AH [Hanbali]"})

# List that contains all the Keys of Narrators of Given Hadith from sanadOrder
extractingKeysFromSanadOrder = []

# Code for Extracting all the Keys of Narrators from sanadOrder based on their status
for i in range(len(statusList)):
    for j in range(len(sanadOrder)):
        if (statusList[i] == sanadOrder[j].get("status")):
            extractingKeysFromSanadOrder.append(sanadOrder[j].get('key'))

# Variable that contains the Reason According to the Nisbat of the Hadith
reasonAccordingToNisbat = ""
# Variable that contains the Type According to the Nisbat of the Hadith
typeAccordingToNisbat = ""


if (1 in extractingKeysFromSanadOrder):
    typeAccordingToNisbat = "Given Hadith is Murfoo."
    reasonAccordingToNisbat = "Because it is narrated from/by Prophet Muhammad (P.B.U.H)."
elif (2 in extractingKeysFromSanadOrder):
    typeAccordingToNisbat = "Given Hadith is Mauqoof."
    reasonAccordingToNisbat = "Because it is narrated from/by Companion (R.A)."
elif (3 in extractingKeysFromSanadOrder):
    typeAccordingToNisbat = "Given Hadith is Maqtoo."
    reasonAccordingToNisbat = "Because it is narrated from/by Follower(Tabi')."
elif (len(narratorsNameList) == 0):
    typeAccordingToNisbat = ""
    reasonAccordingToNisbat = "There is no Narrator in the given Hadith."
else:
    typeAccordingToNisbat = "Given Hadith does not exist in this category."
    reasonAccordingToNisbat = "Because it is neither narrated from/by Prophet Muhammad (P.B.U.H) nor Companion (R.A) nor Follower(Tabi')."

# List that contains Narrator's Names for showing them on Submit Page
showNarratorsList = []


for i in range(len(checkList)):
    dic = {'name': checkList[i].get("name"), 'id': "" + str(checkList[i].get("id"))}
    showNarratorsList.append(dic)

# if(notFoundNarrators!=''):
#     showNarratorsList.append({'name': notFoundNarrators, 'id':0})
# print(finalIdList_Narrators)

myDb = mysql.connector.connect(host="localhost",user="root",passwd="fb834946220403",database="scholar_database")
myCursor = myDb.cursor()

reason_Musnad = ""
reason_Sahih = ""
reason_Zaeef = ""
reason_Munqate = ""
reason_Muedal = ""
reason_Muallaq = ""
reason_Mursal = ""

counter_Musnad = 0
print(finalIdList_Narrators)


for i in range(len(finalIdList_Narrators)):
    if (i <= len(finalIdList_Narrators) - 2):
        query = "select teacher_id from teachers where scholar_id = " + str(finalIdList_Narrators[i]) + ";"

        myCursor.execute(query)

        result = myCursor.fetchall()

        teacher_ids = []
        for j in range(len(result)):
            teacher_ids.append(result[j][0])

        if (finalIdList_Narrators[i + 1] in teacher_ids):
            counter_Musnad += 1
        else:

            query = "select student_id from students where scholar_id = " + str(finalIdList_Narrators[i + 1]) + ";"

            myCursor.execute(query)

            result = myCursor.fetchall()

            student_ids = []
            for k in range(len(result)):
                teacher_ids.append(result[k][0])

            if (finalIdList_Narrators[i] in student_ids):
                counter_Musnad += 1
            else:
                # print("The given hadith is Munqate.")

                query = "select teacher_id from teachers where scholar_id = " + str(finalIdList_Narrators[i]) + ";"

                myCursor.execute(query)

                result1 = myCursor.fetchall()

                munqateTeacherIds1 = []

                for j in range(len(result1)):
                    munqateTeacherIds1.append(result1[j][0])

                isNotPresent1 = 0

                if (finalIdList_Narrators[i + 1] not in munqateTeacherIds1):
                    isNotPresent1 = 1

                if (isNotPresent1):

                    munqateTeacherIds2 = []

                    for k in range(len(munqateTeacherIds1)):

                        query = "select teacher_id from teachers where scholar_id = " + str(
                            munqateTeacherIds1[k]) + ";"

                        myCursor.execute(query)

                        result2 = myCursor.fetchall()

                        for m in range(len(result2)):
                            munqateTeacherIds2.append(result2[m][0])

                    isNotPresent2 = 0

                    if (finalIdList_Narrators[i + 1] not in munqateTeacherIds2):
                        isNotPresent2 = 1

                    if (isNotPresent2):
                        reason_Zaeef = "The given hadith is Zaeef."
                        reason_Muedal = "The given hadith is Muedal because two consecutive narrators are missing."

                    else:
                        reason_Zaeef = "The given hadith is Zaeef."
                        reason_Munqate = "The given hadith is Munqate because chain is broken at some point."

if (counter_Musnad == len(finalIdList_Narrators) - 1 and len(finalIdList_Narrators) > 1):
    if (1 in finalIdList_Narrators):
        reason_Musnad = "The given hadith is Musnad because no narrator is missing from the chain till Prophet (صلی اللہ علیہ وآلہ وسلم)."
        scholarsStatus = []
        for i in range(len(finalIdList_Narrators)):
            query = "select Jarah_Taadeel from scholars where id = " + str(finalIdList_Narrators[i]) + ";"

            myCursor.execute(query)

            result = myCursor.fetchall()

            scholarsStatus.append(result[0][0])

        if ("Zaeef" in scholarsStatus):
            reason_Zaeef="The given hadith is Zaeef."
        else:
            reason_Sahih = "The given hadith is also Sahih."
    else:
        scholarsStatus = []
        for i in range(len(finalIdList_Narrators)):
            query = "select Jarah_Taadeel from scholars where id = " + str(finalIdList_Narrators[i]) + ";"

            myCursor.execute(query)

            result = myCursor.fetchall()

            scholarsStatus.append(result[0][0])

        if ("Zaeef" in scholarsStatus):
            reason_Zaeef="The given hadith is Zaeef."
        else:
            reason_Sahih = "The given hadith is Sahih."

if (len(finalIdList_Narrators) == 1):
    if (1 in finalIdList_Narrators):
        reason_Zaeef = "The given hadith is Zaeef."
        reason_Muallaq = "The given hadith is Muallaq because whole chain of narrators is missing."
print(extractingKeysFromSanadOrder)
if ((extractingKeysFromSanadOrder[-1] == 1) and (extractingKeysFromSanadOrder[-2] == 3)):
    reason_Mursal = "The given hadith is Mursal because Follower(Tabi') is directly narrated from Prophet (صلی اللہ علیہ وآلہ وسلم)."















































