# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 03:35:13 2022

@author: iammu
"""

import pandas as pd

df10 = pd.read_csv('C:/Users/iammu/OneDrive/Desktop/cuisine.csv')

cuisine_description = []

cuisine = []

dataFrameList = list(df10['Column1'])

for i in range(1,len(dataFrameList)):
    index = dataFrameList[i].rfind(",")
    
    cuisine_description.append(dataFrameList[i][0:index].strip())
    
    cuisine.append(dataFrameList[i][index+1:].strip())
    
for i in range(len(cuisine_description)):
    cuisine_description[i] = cuisine_description[i].replace('"','')

df11 = pd.DataFrame(columns=["cuisine_description","cuisine"])

df11["cuisine_description"] = cuisine_description

df11["cuisine"] = cuisine

df11.to_csv("C:/Users/iammu/OneDrive/Desktop/cuisineDatasetForML.csv")
