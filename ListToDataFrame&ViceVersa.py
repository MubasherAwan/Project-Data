# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:56:14 2022

@author: iammu
"""

import pandas as pd

data = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/Final Year Project/Islam360(LatestVersion)/Bukhari/Bukharinew.xlsx")


list_of_ids = list(data['hadees_number'])
list_of_BookName = list(data['BookUR'])
list_of_Bab = list(data['Kitab'])
list_of_Hadith = list(data['without_aeraab'])



df=pd.DataFrame()
df["ids"]=list_of_ids
df["BookName"]=list_of_BookName
df["Bab"]=list_of_Bab


ListSplitter=["رسول الله صلى الله عليه وسلم","النبي صلى الله عليه وسلم","يا رسول الله","محمد صلی اللہ علیہ وآلہ وسلم"]
lstsplit=[]
sanad=''
matn=''
for i in range(len(list_of_Hadith)):
    if(list_of_Hadith[i].__contains__("النبي صلى الله عليه وسلم")):
        lstsplit.append(list_of_Hadith[i].split("النبي صلى الله عليه وسلم",1))
        continue
    if(list_of_Hadith[i].__contains__("رسول الله صلى الله عليه وسلم")):
       lstsplit.append(list_of_Hadith[i].split("رسول الله صلى الله عليه وسلم",1))
       continue
    if(list_of_Hadith[i].__contains__("محمد صلی اللہ علیہ وآلہ وسلم")):
        lstsplit.append(list_of_Hadith[i].split("محمد صلی اللہ علیہ وآلہ وسلم",1))
        continue
    if(list_of_Hadith[i].__contains__("يا رسول الله")):
        lstsplit.append(list_of_Hadith[i].split("يا رسول الله",1))
        continue
   
    


SanadList=[]
for i in range(len(lstsplit)):
    SanadList.append(lstsplit[i][1])
    
        
df["Hadith_Matn"]=SanadList       

        
        

# WordReplace=["حدثني","وحدثنا","حدثنا","نحوه","عن","قال","فقال","سمعت","يقول","أنه","سمع","أخبرني","مولى","أخبرنا","اخبرنا","سال","أن","قالت",":","في حديثه","تابعه","أخبره","ان","انه","اخبرني","على المنبر","رواه","وحدثني","وأخبرني"]
# nameList=[]
# contextList=[]
# for i in range(len(df)):
#     if(i<10):
#         WithoutAhrabTxt=list_of_Hadith[i]
#         txtList=WithoutAhrabTxt.split(" ")
#         string=""
#         nameString=""
#         for i in range(len(txtList)):
    
#             if (txtList[i] in WordReplace) == True:
#                 string+=(txtList[i]+" ")
#                 if(nameString!=""):
#                     nameList.append(nameString)
#                     nameString=""
#             if (txtList[i] in WordReplace) == False:
#                 nameString+=(txtList[i]+" ")
#                 if(string!=""):
#                     contextList.append(string)
#                     string=""
#     else:
#         break

df.to_excel("Bukhari's_Matan.xlsx")
