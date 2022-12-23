# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 00:26:37 2022

@author: Ali Baqar
"""

import mysql.connector

# narratorsIdList = [30418,20005,11062,11213,11042,3,1]

# narratorsIdList = [11013,10567,34]

narratorsIdList = [20340,11243,11709,18,1]

narratorsNameList = ["الحميدي عبد الله بن الزبير","سفيان","يحيى بن سعيد الأنصاري","محمد بن إبراهيم التيمي","علقمة بن وقاص الليثي","عمر بن الخطاب","محمد صلی اللہ علیہ وآلہ وسلم"]

myDb = mysql.connector.connect(host="localhost",user="root",passwd="fb834946220403",database="dummy")

myCursor = myDb.cursor()


# myCursor.close()
# myDb.close()

reason_Musnad = ""
reason_Sahih = ""
reason_Zaeef = ""
reason_Munqate = ""
reason_Muedal = ""
reason_Muallaq = ""
reason_Mursal = ""

counter_Musnad = 0
for i in range(len(narratorsIdList)):
    if(i<=len(narratorsIdList)-2):
        query = "select teacher_id from teachers where scholar_id = "+str(narratorsIdList[i])+";"
        
        myCursor.execute(query)
    
        result = myCursor.fetchall()
    
        teacher_ids = []
        for j in range(len(result)):
            teacher_ids.append(result[j][0])
    
        if(narratorsIdList[i+1] in teacher_ids):
            counter_Musnad+=1
        else:
            
            query = "select student_id from students where scholar_id = "+str(narratorsIdList[i+1])+";"
            
            myCursor.execute(query)
        
            result = myCursor.fetchall()
        
            student_ids = []
            for k in range(len(result)):
                teacher_ids.append(result[k][0])
            
            if(narratorsIdList[i] in student_ids):
                counter_Musnad+=1
            else:
                # print("The given hadith is Munqate.")
                
                query = "select teacher_id from teachers where scholar_id = "+str(narratorsIdList[i])+";"
                
                myCursor.execute(query)
            
                result1 = myCursor.fetchall()
                
                munqateTeacherIds1 = []
                
                for j in range(len(result1)):
                    munqateTeacherIds1.append(result1[j][0])
                
                isNotPresent1 = 0
                
                if(narratorsIdList[i+1] not in munqateTeacherIds1):
                        isNotPresent1 = 1
                
                if(isNotPresent1):
                    
                    munqateTeacherIds2 = []
                    
                    for k in range(len(munqateTeacherIds1)):
                        
                        query = "select teacher_id from teachers where scholar_id = "+str(munqateTeacherIds1[k])+";"
                        
                        myCursor.execute(query)
                    
                        result2 = myCursor.fetchall()
                        
                        for m in range(len(result2)):
                            munqateTeacherIds2.append(result2[m][0])
                    
                    isNotPresent2 = 0
                    
                    if(narratorsIdList[i+1] not in munqateTeacherIds2):
                        
                        isNotPresent2 = 1
                    
                    if(isNotPresent2):
                        reason_Zaeef = "The given hadith is Zaeef."
                        reason_Muedal = "The given hadith is Muedal because two consecutive narrators are missing."
                        
                    else:
                        reason_Zaeef = "The given hadith is Zaeef."
                        reason_Munqate = "The given hadith is Munqate because chain is broken at some point."
                        
                # else:
                    
                #     print("Link Occurred/Not Munqate")
                
                # query = "select teacher_id from teachers where scholar_id = "+str(narratorsIdList[i])+";"
                
                # myCursor.execute(query)
            
                # result1 = myCursor.fetchall()
                
                # munqateTeacherIds = []
                
                # for j in range(len(result1)):
                #     munqateTeacherIds.append(result1[j][0])
                
                # query = "select student_id from students where scholar_id = "+str(narratorsIdList[i+1])+";"
                
                # myCursor.execute(query)
            
                # result2 = myCursor.fetchall()
                
                # munqateStudentIds = []
                
                # for j in range(len(result2)):
                #     munqateStudentIds.append(result2[j][0])
                
                # isPresent = 0
                
                # if(len(munqateTeacherIds)<=len(munqateStudentIds)):
                #     for k in range(len(munqateTeacherIds)):
                #         if(munqateTeacherIds[k] in munqateStudentIds):
                #             isPresent = 1
                #             print("Yes1")
                # else:
                #     for k in range(len(munqateStudentIds)):
                #         if(munqateStudentIds[k] in munqateTeacherIds):
                #             isPresent = 1
                #             print("Yes2")
                
                
                # if(isPresent):
                #     print("One")
                    
                # else:
                #     print("Two")
                
                
                

if(counter_Musnad==len(narratorsIdList)-1 and len(narratorsIdList)>1):
    if(1 in narratorsIdList):
        reason_Musnad = "The given hadith is Musnad because no narrator is missing from the chain till Prophet (صلی اللہ علیہ وآلہ وسلم)."
        scholarsStatus = []
        for i in range(len(narratorsIdList)):
            query = "select Jarah_Taadeel from scholars where id = "+str(narratorsIdList[i])+";"
            
            myCursor.execute(query)
        
            result = myCursor.fetchall()
            
            scholarsStatus.append(result[0][0])
            
        if("Zaeef" in scholarsStatus):
            print("Here")
        else:
            reason_Sahih = "The given hadith is also Sahih."
    else:
        scholarsStatus = []
        for i in range(len(narratorsIdList)):
            query = "select Jarah_Taadeel from scholars where id = "+str(narratorsIdList[i])+";"
            
            myCursor.execute(query)
        
            result = myCursor.fetchall()
            
            scholarsStatus.append(result[0][0])
            
        if("Zaeef" in scholarsStatus):
            print("Here")
        else:
            reason_Sahih = "The given hadith is Sahih."


if(len(narratorsIdList)==1):
    if(1 in narratorsIdList):
        reason_Zaeef = "The given hadith is Zaeef."
        reason_Muallaq = "The given hadith is Muallaq because whole chain of narrators is missing."
            
            
            
            
            
statusList = []            
for i in range(len(narratorsIdList)):      
    query = "select status from scholars where id = "+str(narratorsIdList[i])+";"
    
    myCursor.execute(query)
    
    result = myCursor.fetchall()

    for j in range(len(result)):
        statusList.append(result[j][0])
            

# Code not for copy
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
    for j in range(len(sanadOrder)):
        if (statusList[i] == sanadOrder[j].get("status")):
            extractingKeysFromSanadOrder.append(sanadOrder[j].get('key'))

if((extractingKeysFromSanadOrder[-1]==1) and (extractingKeysFromSanadOrder[-2]==3)):
    reason_Mursal = "The given hadith is Mursal because Follower(Tabi') is directly narrated from Prophet (صلی اللہ علیہ وآلہ وسلم)."
            
            
            
            
print(reason_Musnad)
print(reason_Sahih)
print(reason_Zaeef)
print(reason_Munqate)
print(reason_Muedal)
print(reason_Muallaq)
print(reason_Mursal )              