# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:02:17 2022

@author: iammu
"""

import pandas as pd


# Function for Checking Presence and Absence of Entries with their length between Two Lists (1D or 2D)
# and return (presentNames, length_presentNames, absentNames, length_absentNames)
def checkEntries_PresentAbsent_withLength_btwTwoLists(listToBeChecked,listWithinCheck):
    presentNames = []
    
    absentNames = []
    
    length_presentNames = []
    
    length_absentNames = []
    
    for i in range(len(listToBeChecked)):
        first_index = listToBeChecked[i]
        if(type(first_index[0])==list):
            presentLength = ""
            absentLength = ""
            dummy_multiplePresentName = []
            dummy_multipleAbsentName = []
            for j in range(len(first_index)):
                dummy_presentName = []
                dummy_absentName = []
                for name1 in first_index[j]:
                    if(name1 in listWithinCheck[i][j]):
                        dummy_presentName.append(name1)
                    else:
                        dummy_absentName.append(name1)
                if(len(dummy_presentName)!=0):
                    dummy_multiplePresentName.append(dummy_presentName)
                    if(j!=len(first_index)-1):
                        presentLength = presentLength +str(len(dummy_presentName)) + ", "
                    else:
                        presentLength = presentLength +str(len(dummy_presentName))
                else:
                    dummy_multiplePresentName.append(["No Name Present"])
                    if(j!=len(first_index)-1):
                        presentLength = presentLength + "0" + ", "
                    else:
                        presentLength = presentLength + "0" 
                    
                if(len(dummy_absentName)!=0):
                    dummy_multipleAbsentName.append(dummy_absentName)
                    if(j!=len(first_index)-1):
                        absentLength = absentLength +str(len(dummy_absentName)) + ", "
                    else:
                        absentLength = absentLength +str(len(dummy_absentName)) 
                else:
                    dummy_multipleAbsentName.append(["No Name Absent"])
                    if(j!=len(first_index)-1):
                        absentLength = absentLength + "0" + ", "
                    else:
                        absentLength = absentLength + "0" 
            presentNames.append(dummy_multiplePresentName)
            absentNames.append(dummy_multipleAbsentName)
            length_presentNames.append(presentLength)
            length_absentNames.append(absentLength)
        else:
            dummy_presentName = []
            dummy_absentName = []
            for name in first_index:
                if(name in listWithinCheck[i]):
                    dummy_presentName.append(name)
                else:
                    dummy_absentName.append(name)
            if(len(dummy_presentName)!=0):
                presentNames.append(dummy_presentName)
                length_presentNames.append(len(dummy_presentName))
            else:
                presentNames.append(["No Name Present"])
                length_presentNames.append(0)
                
            if(len(dummy_absentName)!=0):
                absentNames.append(dummy_absentName)
                length_absentNames.append(len(dummy_absentName))
            else:
                absentNames.append(["No Name Absent"])
                length_absentNames.append(0)
    
    return (presentNames, length_presentNames, absentNames, length_absentNames)
# ****************************************************************************************************


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


df = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/comparison/Overall Comparison (after removing error in rule-based)/Exact_RuleBased_OldNER_NewNERNames.xlsx")

df1 = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/comparison/Overall Comparison (after removing error in rule-based)/LengthComparison_Exact_RuleBased_OldNER_andNewNERNamesFrom480Hadith.xlsx")


exactNamesList = extractListsFrom_ListFormattedStrings(list(df["Exact_Names"]))

newNERNamesList = extractListsFrom_ListFormattedStrings(list(df["NewNERNames"]))


newNER_presentNamesIn_E , newNER_lengthPresentNamesIn_E, newNER_absentNamesIn_E, newNER_lengthAbsentNamesIn_E = checkEntries_PresentAbsent_withLength_btwTwoLists(newNERNamesList, exactNamesList)

df2 = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/comparison/NewNERandExactNames/NamesAndLengthComparison_NewNER_andExactNamesFrom480Hadith.xlsx")

df2["ExactNames"] = df["Exact_Names"]

df2["length_ExactNames"] = df1["Length_ExactNames"]

df2["new_NERNames"] = df["NewNERNames"]

df2["Length_NewNERNames"] = df1["Length_NewNERNames"]


df2["NamePresentInNewNER"] = newNER_presentNamesIn_E

df2["Length_PresentNames"] = newNER_lengthPresentNamesIn_E

df2["NameAbsentInNewNER"] = newNER_absentNamesIn_E

df2["Length_AbsentNames"] = newNER_lengthAbsentNamesIn_E

df2.to_excel("C:/Users/iammu/OneDrive/Desktop/comparison/NewNERandExactNames/NamesAndLengthComparison_NewNER_andExactNamesFrom480Hadith.xlsx")











