# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 18:30:58 2022

@author: iammu
"""

import pandas as pd

textFile = open("C:/Users/iammu/OneDrive/Desktop/Text(Deewan ul Zuefa).txt","r",encoding='utf-8')

textFileData = textFile.read()
textFileLinesList=textFileData.split("\n")
refinedTextFileLinesList=[]
for i in range(len(textFileLinesList)):
    if(len(textFileLinesList[i].split())==0 or len(textFileLinesList[i].split())==1):
        continue
    else:
        refinedTextFileLinesList.append(textFileLinesList[i])


narratorId=[]
narratorName=[]
narratorStatus=[]
scholarOrReviewerName=[]
for i in range(len(refinedTextFileLinesList)):
    if(refinedTextFileLinesList[i].count(":")==1):
        dum = refinedTextFileLinesList[i].split(":")
        dum0 = dum[0].split("-")
        narratorId.append(dum0[0])
        narratorName.append(dum0[1])
        narratorStatus.append(dum[1])
        scholarOrReviewerName.append("No Scholar/Viewer")
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
        


