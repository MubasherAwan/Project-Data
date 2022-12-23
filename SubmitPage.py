# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 14:10:20 2022

@author: iammu
"""
import mysql.connector
import pandas as pd

#hadithText = request.POST.get('text', '')
hadithText='''حَدَّثَنَا الْحُمَيْدِيُّ عَبْدُ اللَّهِ بْنُ الزُّبَيْرِ ، قَالَ : حَدَّثَنَا سُفْيَانُ ، قَالَ : حَدَّثَنَا يَحْيَى بْنُ سَعِيدٍ الْأَنْصَارِيُّ ، قَالَ : أَخْبَرَنِي مُحَمَّدُ بْنُ إِبْرَاهِيمَ التَّيْمِيُّ ، أَنَّهُ سَمِعَ عَلْقَمَةَ بْنَ وَقَّاصٍ اللَّيْثِيَّ ، يَقُولُ : سَمِعْتُ عُمَرَ بْنَ الْخَطَّابِ رَضِيَ اللَّهُ عَنْهُ عَلَى الْمِنْبَرِ، قَالَ : سَمِعْتُ رَسُولَ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ، يَقُولُ : " إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ، وَإِنَّمَا لِكُلِّ امْرِئٍ مَا نَوَى، فَمَنْ كَانَتْ هِجْرَتُهُ إِلَى دُنْيَا يُصِيبُهَا أَوْ إِلَى امْرَأَةٍ يَنْكِحُهَا، فَهِجْرَتُهُ إِلَى مَا هَاجَرَ إِلَيْهِ'''
WordReplace=["حدثني","وحدثنا","حدثنا","نحوه","عن","قال","فقال","سمعت","يقول","أنه","سمع","أخبرني","مولى","أخبرنا","اخبرنا","سال","أن","قالت",":","في حديثه","تابعه","أخبره","ان","انه","اخبرني","وحدثني","وأخبرني"]

# keys = ["وحدثنا", "حدثنا", "نحوه", "عن", "قال", "فقال", "سمعت", "يقول", "أنه", "سمع", "أخبرني", "مولى", "أن",
    #                "أخبرنا", "في حديثه", "تابعه", "انه", "اخبرني", "وأخبرني"]

ListSplitter = ["رسول الله صلى الله عليه وسلم", "النبي صلى الله عليه وسلم", "يا رسول الله",
                    "محمد صلی اللہ علیہ وآلہ وسلم"]

contextList = []
nameList = []
#finalName = []

WithoutAhrabTxt = ""

#Aeraab Remover Code
for i in range(len(hadithText)):
    no = ord(hadithText[i])
    if(no==1614 or no==1615 or no==1616 or no==1618 or no==1617 or no==1612 or no==1613 or no==1611):
        continue
    else:
        WithoutAhrabTxt += hadithText[i]

txtList = WithoutAhrabTxt.split(" ")

#Extracting Scholars_name and Context of Narration
string = ""
nameString = ""
for i in range(len(txtList)):

    if (txtList[i] in WordReplace) == True:
        string += (txtList[i] + " ")
        if (nameString != ""):
            nameList.append(nameString)
            nameString = ""
    if (txtList[i] in WordReplace) == False:
        nameString += (txtList[i] + " ")
        if (string != ""):
            contextList.append(string)
            string = ""

for i in range(len(ListSplitter)):
    if (ListSplitter[i] not in nameList and nameString.__contains__(ListSplitter[i])):
        nameList.append("محمد صلی اللہ علیہ وآلہ وسلم")

for i in range(len(nameList)):
    for j in range(len(ListSplitter)):
        if (nameList[i].__contains__(ListSplitter[j]) and nameList[i] != ListSplitter[j]):
            nameList[i] = "محمد صلی اللہ علیہ وآلہ وسلم"

nameList = list(dict.fromkeys(nameList))


FinalIdList = []
finalIds = []
checkList = []
#Cross Check of Narrators_Names with Database
for i in range(len(nameList)):
    
    #Database Connectivity
    myDb = mysql.connector.connect(host="localhost", user="root", passwd="fb834946220403", database="dummy")
    myCursor = myDb.cursor()

    nameList[i] = nameList[i].replace('''"''', '')
    nameList[i] = nameList[i].replace("ـ رضى الله عنها ـ", "")
    nameList[i] = nameList[i].replace("ـ رضى الله عنهما ـ", "").strip()

    if (nameList[i][-1] != "،"):
        twoNameList = nameList[i].split("،")
        for dum in range(len(twoNameList)):
            query = '''select * from scholar_other_names
                        where name like "''' + twoNameList[dum].strip() + '''";'''
            myCursor.execute(query)
            result = myCursor.fetchall()
            print(result)
            if (len(result) != 0):
                FinalIdList.append(result[0])
                break

            query = '''select * from scholars
                     where name like "''' + twoNameList[dum].strip() + '''";'''
            myCursor.execute(query)
            result = myCursor.fetchall()
            if (len(result) != 0):
                FinalIdList.append(result[0])
    else:

        nameList[i] = nameList[i].replace("،", "")
        nameList[i] = nameList[i].replace("على المنبر", "")
        nameList[i] = nameList[i].replace("رضي الله عنها", "")
        nameList[i] = nameList[i].replace("رضي الله عنه", "")
        nameList[i] = nameList[i].strip()
        print(nameList[i])
        query = '''select * from scholars
                     where name like "''' + nameList[i] + '''";'''
        myCursor.execute(query)
        result = myCursor.fetchall()
        if (len(result) != 0):
            FinalIdList.append(result[0])

        if (len(result) == 0):
            query = '''select * from scholar_other_names
                      where name like "''' + nameList[i] + '''";'''
            myCursor.execute(query)
            result = myCursor.fetchall()
            if (len(result) != 0):
                FinalIdList.append(result[0])
    for j in range(len(FinalIdList)):
        for k in (FinalIdList[j]):
            if (len(FinalIdList[j]) == 7):
                finalIds.append(FinalIdList[j][0])
                # print(FinalIdList[j][0])
                break
            if (len(FinalIdList[j]) == 3):
                finalIds.append(FinalIdList[j][1])
                # print(FinalIdList[j][1])
                break

#Combine Scholar_Ids and Scholar_Names in a Dictionary
for flst in range(len(FinalIdList)):
    if (len(FinalIdList[flst]) == 7):
        dum = FinalIdList[flst][0]
        dum1 = FinalIdList[flst][1]
        dumDict = {'id': dum, 'name': dum1}
        checkList.append(dumDict)
        dum1 = ''
        dum = ''
        dumDict = {}

    if (len(FinalIdList[flst]) == 3):
        dum = FinalIdList[flst][1]
        dum1 = FinalIdList[flst][2]
        dumDict = {'id': dum, 'name': dum1}
        checkList.append(dumDict)
        dum1 = ''
        dum = ''
        dumDict = {}

#EXtracting Status_of_Narrators from Database using Scholar_Ids
statusList = []
for i in range(len(checkList)):
    query = '''select status from scholars
             where id = ''' + str(checkList[i].get("id")) + ''';'''
    myCursor.execute(query)
    result = myCursor.fetchall()
    statusList.append(result[0])
    print(str(statusList[i]))

#Categorized Scholars According to their status
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

extractingKeysFromSanadOrder = []
for i in range(len(statusList)):
    for j in statusList[i]:
        for k in range(len(sanadOrder)):
            if (j == sanadOrder[k].get("status")):
                extractingKeysFromSanadOrder.append(sanadOrder[k].get('key'))

reasonAccordingToNisbat = ""
typeAccordingToNisbat = ""
if (1 in extractingKeysFromSanadOrder):
    typeAccordingToNisbat = "Murfoo"
    reasonAccordingToNisbat = "Prophet Muhammad (P.B.U.H)."
elif (2 in extractingKeysFromSanadOrder):
    typeAccordingToNisbat = "Mauqoof"
    reasonAccordingToNisbat = "Companion (R.A)."
elif (3 in extractingKeysFromSanadOrder):
    typeAccordingToNisbat = "Maqtoo"
    reasonAccordingToNisbat = "Follower(Tabi')."

refineIdList = []

for i in range(len(extractingKeysFromSanadOrder)):
    #print(dumm[i])
    if (extractingKeysFromSanadOrder[i] != 1):
        refineIdList.append(extractingKeysFromSanadOrder[i])
    else:
        refineIdList.append(extractingKeysFromSanadOrder[i])
        break

checkMunqate = 0
reasonOfMunqate = ''
missingIdsOfNarrators = []

if (checkMunqate == 0):
    checkMunqate = refineIdList[0]

for i in range(len(refineIdList)):
    if (checkMunqate == 1):
        break
    elif (refineIdList[i] == checkMunqate):
        continue
    elif (refineIdList[i] == checkMunqate - 1):
        checkMunqate = checkMunqate - 1
    elif (refineIdList[i] == checkMunqate - 2):
        missingIdsOfNarrators.append(refineIdList[i] + 1)
        checkMunqate = checkMunqate - 2
    elif (refineIdList[i] == checkMunqate - 3):
        missingIdsOfNarrators.append(refineIdList[i] + 2)
        missingIdsOfNarrators.append(refineIdList[i] + 1)
        checkMunqate = checkMunqate - 3
    elif (refineIdList[i] == checkMunqate - 4):
        missingIdsOfNarrators.append(refineIdList[i] + 3)
        missingIdsOfNarrators.append(refineIdList[i] + 2)
        missingIdsOfNarrators.append(refineIdList[i] + 1)
        checkMunqate = checkMunqate - 4
    elif (refineIdList[i] == checkMunqate - 5):
        missingIdsOfNarrators.append(refineIdList[i] + 4)
        missingIdsOfNarrators.append(refineIdList[i] + 3)
        missingIdsOfNarrators.append(refineIdList[i] + 2)
        missingIdsOfNarrators.append(refineIdList[i] + 1)
        checkMunqate = checkMunqate - 5

if (len(missingIdsOfNarrators) != 0):
    for i in range(len(missingIdsOfNarrators)):
        for j in range(len(sanadOrder)):
            if ((missingIdsOfNarrators[i]) == sanadOrder[j].get("key")):
                if (i == len(missingIdsOfNarrators) - 1):
                    reasonOfMunqate = reasonOfMunqate + (sanadOrder[j].get("status"))
                    break
                else:
                    reasonOfMunqate = reasonOfMunqate + (sanadOrder[j].get("status")) + " / "
                    break


showList = []
for i in range(len(checkList)):
    dic = {'name': checkList[i].get("name"), 'id': ""+str(checkList[i].get("id"))}
    showList.append(dic)
type = ""
reason = ""
counter = -1
for i in contextList:
    if(i=="،" or i==":" or i=="،:" or i==":،"):
        continue
    else:
        counter += 1
if(counter<=2):
    type = "Gareeb"
    reason = "Because it has two or less than two narrator"
elif (counter >= 3 and counter<=4):
    type = "Aziz"
    reason = "Because it has three or less than four narrators"
elif (counter >= 5):
    type = "Mashhur"
    reason = "Because it has five or more than five narrators"
if(len(reasonOfMunqate)!=0):
    reasonOfMunqate = "Given Hadith is Munqate Because it has missing " + reasonOfMunqate
    params = {'hadithText': WithoutAhrabTxt, 'list': showList,'type':type,'reason':reason,'typeAccordingToNisbat':typeAccordingToNisbat,'reasonAccordingToNisbat':reasonAccordingToNisbat,'reasonOfMunqate':reasonOfMunqate}
else:
    params = {'hadithText': WithoutAhrabTxt, 'list': showList, 'type': type, 'reason': reason,'typeAccordingToNisbat': typeAccordingToNisbat, 'reasonAccordingToNisbat': reasonAccordingToNisbat}
