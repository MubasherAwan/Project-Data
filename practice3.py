# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 09:50:56 2022

@author: Lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 18:30:58 2022

@author: iammu
"""

import pandas as pd

textFile = open("C:/Users/iammu/OneDrive/Desktop/Data/practice3.txt","r",encoding='utf-8')

textFileData = textFile.read()
textFileLinesList=textFileData.split("\n")
refinedTextFileLinesList=[]
for i in range(len(textFileLinesList)):
    if(len(textFileLinesList[i].split())==0 or len(textFileLinesList[i].split())==1):
        continue
    else:
        refinedTextFileLinesList.append(textFileLinesList[i])

afterColon=[]
narratorId=[]
narratorName=[]
narratorStatus=[]
scholarOrReviewerName=[]
#dum2=[]
for i in range(len(refinedTextFileLinesList)):
    afterColon=[]
    if(refinedTextFileLinesList[i].count(":")==1):
        dum = refinedTextFileLinesList[i].split(":")
        dum0 = dum[0].split("-")
       # dum1 = dum[1].split(",")
        #narratorStatus.append(dum1[1])
        narratorId.append(dum0[0])
        narratorName.append(dum0[1])
        afterColon.append(dum[1])
        if(afterColon.count("،")==3):
        #if(dum[1].__contains__("،")):
            dum1 = dum[1].split("،")
            if(dum1[0].__contains__("عن")):
                dum2=dum1[0].split("عن")
                scholarOrReviewerName.append(dum2[1])
                narratorStatus.append(dum1[2])
                narratorStatus.append(dum1[3])
            elif(dum1[1].__contains__("عن")):
              dum2=dum1[1].split("عن")
              scholarOrReviewerName.append(dum2[1])
              narratorStatus.append(dum1[2])
              narratorStatus.append(dum1[3]) 
        elif(afterColon.count("،")==2):
            dum1 = dum[1].split("،")
            if(dum1[1].__contains__("عن")):
                dum2=dum1[1].split("عن") 
                scholarOrReviewerName.append(dum2[1])
                narratorStatus.append(dum1[2])
            elif(dum1[1].__contains__("عنه")):
               dum2=dum1[1].split("عنه")
               scholarOrReviewerName.append(dum2[1])
               narratorStatus.append(dum1[2])
            elif(dum1[0].__contains__("ذكره")):
                dum2=dum1[0].split("ذكره")
                scholarOrReviewerName.append(dum2[1])
                narratorStatus.append(dum1[2])
                narratorStatus.append(dum1[1])
            elif(dum1[1].__contains__("تكلم فيه")):
                dum2=dum1[0].split("تكلم فيه")
                scholarOrReviewerName.append(dum2[1])
                narratorStatus.append(dum1[0])
                narratorStatus.append("تكلم فيه")
            elif(dum1[1].__contains__("ه")):
                dum2=dum1[0].split("ه")
                scholarOrReviewerName.append(dum2[1])
                narratorStatus.append(dum1[0])
                narratorStatus.append(dum1[1])
            elif(dum1[0].__contains__("عن")):
                dum2=dum1[0].split("عن") 
                scholarOrReviewerName.append(dum2[1])
                narratorStatus.append(dum1[2]) 
                narratorStatus.append(dum1[1])
            elif(dum1[0].__contains__("عن"))==False:
                scholarOrReviewerName.append(dum2[1])
                narratorStatus.append(dum1[1]) 
            elif(dum1[0]and dum1[1].__contains__("عن")):
                 dum2= dum1[1].split("عن")
                 scholarOrReviewerName.append(dum2[1])
                 narratorStatus.append(dum1[2])
        elif(afterColon.count("،")==1): 
            dum1=dum[1].split("،")
            scholarOrReviewerName.append(dum1[0])
            narratorStatus.append(dum1[1])
            if(dum1[1].__contains__("ه")):
                dum2= dum1[1].split("ه")
                scholarOrReviewerName.append("imam zahbi")
                narratorStatus.append(dum1[1])
                narratorStatus.append(dum2[0])
            elif(dum1[1].__contains__("روى عنه")):
                dum2= dum1[1].split("روى عنه")
                scholarOrReviewerName.append(dum2[1])
                narratorStatus.append(dum1[0])
            elif(dum1[1].__contains__("روى عنه")):
                 dum2= dum1[1].split("روى عنه")
                 scholarOrReviewerName.append(dum2[1])
                 narratorStatus.append(dum1[0])
            elif(dum1[0].__contains__("عن")):
                 dum2=dum1[0].split("عن") 
                 scholarOrReviewerName.append(dum2[1])
                 narratorStatus.append(dum1[1]) 
            elif(dum1[0].__contains__("هو")):
                  dum2=dum1[0].split("هو") 
                  scholarOrReviewerName.append(dum2[1])
                  narratorStatus.append(dum1[1]) 
            elif(dum1[0].__contains__("لم يتكلم فيه")):
                 dum2=dum1[0].split("لم يتكلم فيه") 
                 scholarOrReviewerName.append(dum2[1])
                 narratorStatus.append(dum1[0])
            elif(dum1[0].__contains__("حدث")):
                 dum2=dum1[0].split("حدث") 
                 scholarOrReviewerName.append(dum2[1])
                 narratorStatus.append(dum1[1])
            elif(dum1[1].__contains__("ه")):
                 dum2= dum1[1].split("ه")
                 scholarOrReviewerName.append(dum2[0])
                 narratorStatus.append(dum2[1])
            elif(dum1[0].__contains__("عنه")):
                 dum2= dum1[0].split("عنه")
                 scholarOrReviewerName.append(dum2[1])
                 narratorStatus.append(dum1[1]) 
            elif(dum1[1].__contains__("له")):
                  scholarOrReviewerName.append("imam zahbi")
                  narratorStatus.append(dum1[0]) 
        elif(afterColon.__contains__(".")):
             dum1=dum[1].split(".")
             if(dum1[0].__contains__("عن")):
                 dum2= dum1[0].split("عن")
                 scholarOrReviewerName.append(dum2[1])
                 narratorStatus.append(dum1[1]) 
             else:
                 scholarOrReviewerName.append("imam zahbi")
                 narratorStatus.append(dum1[1]) 
                 
             if(afterColon.__contains__("ه")):
                  dum1=dum[1].split("ه")
                  scholarOrReviewerName.append(dum1[1])
                  narratorStatus.append(dum1[0]) 
             else:
               scholarOrReviewerName.append("imam zahbi")
               narratorStatus.append(dum[1]) 
    elif(refinedTextFileLinesList[i].count(":")==2):
        dum = refinedTextFileLinesList[i].split(":")
        dum0 = dum[0].split("-")
        narratorId.append(dum0[0])
        narratorName.append(dum0[1])
        narratorStatus.append(dum[2])
        if(dum[1].__contains__("قال")):
            dum1 = dum[1].split("قال")
            scholarOrReviewerName.append(dum1[1])
        elif(dum[1].__contains__("عن")):
            dum1 = dum[1].split("عن")
            scholarOrReviewerName.append(dum1[1])
    elif(refinedTextFileLinesList[i].count(":")==3):
        dum = refinedTextFileLinesList[i].split(":")
        dum0 = dum[0].split("-")
        narratorId.append(dum0[0])
        narratorName.append(dum0[1])
        narratorStatus.append(dum[3])
        if(dum[1].__contains__("قال")):
            dum1 = dum[1].split("قال")
            scholarOrReviewerName.append(dum1[1])
        elif(dum[2].__contains__("قال")):
            dum2 = dum[2].split("قال")
            scholarOrReviewerName.append(dum2[1])
        elif(dum[1].__contains__("عن")):
            dum1 = dum[1].split("عن")
            scholarOrReviewerName.append(dum1[1])
        elif(dum[2].__contains__("عن")):
            dum2 = dum[2].split("عن")
            scholarOrReviewerName.append(dum2[1])
        #     narratorStatus.append(dum1[1])
        
        #     if (dum[0].__contains__("عن")):
        #      dum2 = dum1[0].split("عن")
        #      scholarOrReviewerName.append(dum2[1])
        # if(dum[1].__contains__(".")):
        #      dum1 = dum[1].split(".")
        #      narratorStatus.append(dum1[1])
         
        # elif (dum[0].__contains__("عن")):
        #      dum2 = dum1[0].split("عن")
        #      scholarOrReviewerName.append(dum2[1])
          
              
    
    