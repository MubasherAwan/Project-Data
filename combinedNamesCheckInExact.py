# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 16:36:50 2022

@author: iammu
"""

import pandas as pd

df4 = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/comparison/CombinedRuleBasedAndNewNERWithExactNames/NamesAndLengthComparison_RuleBased_afterApplingNewNER_withExactNamesFrom480Hadith.xlsx")

#Function for extracting Lists from 'List Formatted Strings'
def extractListsFrom_ListFormattedStrings(dummy):
    finalNamesList = []
    for i in range(len(dummy)):
        dum = dummy[i]
        if(dum.count("[")==1):
            dum=dum.replace("[","")
            dum=dum.replace("]","")
            dum=dum.replace("'","")
            dumList = dum.split(",")
            dumList = [item.strip() for item in dumList]
            finalNamesList.append(dumList)
        else:
            separateList = dum.split("],")
            multipleLists = []
            for i in range(len(separateList)):
                index = separateList[i]
                index=index.replace("[","")
                index=index.replace("]","")
                index=index.replace("'","")
                indList = index.split(",")
                indList = [item.strip() for item in indList]
                multipleLists.append(indList)
            finalNamesList.append(multipleLists)
    return finalNamesList
#***********************************************************


exactNamesList = extractListsFrom_ListFormattedStrings(list(df4["ExactNames"]))

checkAbsentNamesWithNewNER = extractListsFrom_ListFormattedStrings(list(df4["CheckAbsentNamesWithNewNER"]))

final_rAfterNER_NamesPresentInExact = []
length_final_rAfterNER_NamesPresentInExact = []
for i in range(len(checkAbsentNamesWithNewNER)):
    if(type(checkAbsentNamesWithNewNER[i][0])==str):
        if(checkAbsentNamesWithNewNER[i][0]==""):
            final_rAfterNER_NamesPresentInExact.append([""])
            length_final_rAfterNER_NamesPresentInExact.append("0")
        else:
            presentNames_SingleList = []
            for j in checkAbsentNamesWithNewNER[i]:
                if(j in exactNamesList[i]):
                    presentNames_SingleList.append(j)
            final_rAfterNER_NamesPresentInExact.append(presentNames_SingleList)
            length_final_rAfterNER_NamesPresentInExact.append(len(presentNames_SingleList))
            
    else:
        
        first_index = checkAbsentNamesWithNewNER[i]
        presentNames_MultipleList = []
        presentLength =""
        for j in range(len(first_index)):
            dummyPresentNames = []
            for name in first_index[j]:
                if(name==""):
                    dummyPresentNames.append([""])
                    if(j!=len(first_index)-1):
                        presentLength = presentLength + "0" + ", "
                    else:
                        presentLength = presentLength + "0"
                else:
                    if(name in exactNamesList[i][j]):
                        dummyPresentNames.append(name)
                    
                    
            if(len(dummyPresentNames)!=0):
                presentNames_MultipleList.append(dummyPresentNames)
                if(j!=len(first_index)-1):
                    presentLength = presentLength +str(len(dummyPresentNames)) + ", "
                else:
                    presentLength = presentLength +str(len(dummyPresentNames))
                
            else:
                presentNames_MultipleList.append([""])
                
                if(j!=len(first_index)-1):
                    presentLength = presentLength + "0" + ", "
                else:
                    presentLength = presentLength + "0"
                
                
        final_rAfterNER_NamesPresentInExact.append(presentNames_MultipleList)
        length_final_rAfterNER_NamesPresentInExact.append(presentLength)


















final_rAfterNER_NamesPresentInExact = []
length_final_rAfterNER_NamesPresentInExact = []

if(type(checkAbsentNamesWithNewNER[9][0])==str):
    if(checkAbsentNamesWithNewNER[9][0]==""):
        final_rAfterNER_NamesPresentInExact.append([""])
        length_final_rAfterNER_NamesPresentInExact.append("0")
        
    else:
        presentNames_SingleList = []
        for j in checkAbsentNamesWithNewNER[9]:
            if(j in exactNamesList[i]):
                presentNames_SingleList.append(j)
        final_rAfterNER_NamesPresentInExact.append(presentNames_SingleList)
        length_final_rAfterNER_NamesPresentInExact.append(len(presentNames_SingleList))
        
else:
    
    first_index = checkAbsentNamesWithNewNER[9]
    presentNames_MultipleList = []
    presentLength =""
    for j in range(len(first_index)):
        dummyPresentNames = []
        for name in first_index[j]:
            print(name)
            if(name==""):
                dummyPresentNames.append([""])
                if(j!=len(first_index)-1):
                    presentLength = presentLength + "0" + ", "
                else:
                    presentLength = presentLength + "0"
            else:
                if(name in exactNamesList[i][j]):
                    dummyPresentNames.append(name)
                
                
        if(len(dummyPresentNames)!=0):
            presentNames_MultipleList.append(dummyPresentNames)
            if(j!=len(first_index)-1):
                presentLength = presentLength +str(len(dummyPresentNames)) + ", "
            else:
                presentLength = presentLength +str(len(dummyPresentNames))
            
        else:
            presentNames_MultipleList.append([""])
            
            if(j!=len(first_index)-1):
                presentLength = presentLength + "0" + ", "
            else:
                presentLength = presentLength + "0"
            
            
    final_rAfterNER_NamesPresentInExact.append(presentNames_MultipleList)
    length_final_rAfterNER_NamesPresentInExact.append(presentLength)




#########################################################
final_rAfterNER_NamesPresentInExact = []
length_final_rAfterNER_NamesPresentInExact = []
for name in range(len(checkAbsentNamesWithNewNER)):
    length=0
    if(type(checkAbsentNamesWithNewNER[name][0])==str):
        if(checkAbsentNamesWithNewNER[name][0]==""):
            final_rAfterNER_NamesPresentInExact.append([""])
            length_final_rAfterNER_NamesPresentInExact.append(length)
            
        else:
            presentNames_SingleList = []
            for j in checkAbsentNamesWithNewNER[name]:
                if(j in exactNamesList[name]):
                    length=length+1
                    presentNames_SingleList.append(j)
                    print(j)
            final_rAfterNER_NamesPresentInExact.append(presentNames_SingleList)
            length_final_rAfterNER_NamesPresentInExact.append(length)
    else:
        index = checkAbsentNamesWithNewNER[name]
        multiList=[]
        multiLength=[]
        for i in range(len(index)):
            dum=[]
            length=0
            for j in range(len(index[i])):
                if(index[i][j]==""):
                    dum.append("")
                    print("Nothing")
                else:
                    if(index[i][j] in exactNamesList[name][i]):
                        dum.append(index[i][j])
                        length=length+1
                        print(index[i][j])
            multiList.append(dum)
            multiLength.append(length)
            
        final_rAfterNER_NamesPresentInExact.append(multiList)
        length_final_rAfterNER_NamesPresentInExact.append(multiLength)
    
            
df4["rAfterNER_NamesPresentInExact"] =final_rAfterNER_NamesPresentInExact

df4["Length_rAfterNER_NamesPresent"] = length_final_rAfterNER_NamesPresentInExact              





df5 =pd.read_excel("C:/Users/iammu/OneDrive/Desktop/comparison/CombinedRuleBasedAndNewNERWithExactNames/NamesAndLengthComparison_RuleBased_afterApplingNewNER_withExactNamesFrom480Hadith.xlsx")

length_ExactNames = list(df5["length_ExactNames"])

length_PresentNamesInExact = list(df5["Length_PresentNames"])

length_rAfterNERNames = list(df5["Length_rAfterNER_NamesPresent"])

# exactNamesList = extractListsFrom_ListFormattedStrings(list(df5["ExactNames"]))


# for i in range(len(length_rAfterNERNames)):
#     if(type(length_rAfterNERNames[i])==str):
#         # length_rAfterNERNames[i] = length_rAfterNERNames[i].replace("[","")
#         # length_rAfterNERNames[i] = length_rAfterNERNames[i].replace("]","")
#         length_rAfterNERNames[i] = length_rAfterNERNames[i].strip()
#         length_ExactNames[i] = length_ExactNames[i].strip()
#         length_PresentNamesInExact[i] = length_PresentNamesInExact[i].strip()

matchorNotMatchList = []
for i in range(len(length_ExactNames)):
    if(type(length_rAfterNERNames[i])==int):
        if(length_PresentNamesInExact[i] + length_rAfterNERNames[i]==length_ExactNames[i]):
            matchorNotMatchList.append(1)
        else:
            matchorNotMatchList.append(0)
    else:
        if((int(length_PresentNamesInExact[i][0]) + int(length_rAfterNERNames[i][0])==int(length_ExactNames[i][0])) and (int(length_PresentNamesInExact[i][-1]) + int(length_rAfterNERNames[i][-1])==int(length_ExactNames[i][-1]))):
            matchorNotMatchList.append(1)
        else:
            matchorNotMatchList.append(0)


df5['Match_Or_Not'] = matchorNotMatchList


df5.to_excel("C:/Users/iammu/OneDrive/Desktop/comparison/CombinedRuleBasedAndNewNERWithExactNames/NamesAndLengthComparison_RuleBased_afterApplingNewNER_withExactNamesFrom480Hadith.xlsx")

