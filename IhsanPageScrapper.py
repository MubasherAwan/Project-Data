# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 02:20:50 2022

@author: iammu
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pandas as pd
import time
pageList=[]



driver = webdriver.Chrome('C:/Users/iammu/chromedriver.exe')


for i in range(4954,5352,2):
    page=driver.get("https://www.ihsanetwork.org/HDBService.asmx/GetHadith2?textNum="+str(i)+"")

    htmlText=driver.find_element_by_class_name('pretty-print')


    pageText=htmlText.get_attribute('innerHTML')

    pageList.append(pageText)


df=pd.DataFrame()
df.to_excel("Starting5352Referencedata.xlsx")










# lists=pageText.split("Entities")
# print(len(lists))
# if(len(lists)==1):
#     print(len(lists))
# else:
   
    
#     # Code for Narrators Name...
#     flag = True
#     withoutTagsText = ""
#     for i in lists[1]:
#         if(i=="<"):
#             flag = False
#         if(flag):
#             withoutTagsText += i
#         if(i==">"):
#             flag=True
    
    
#     withoutTagsText = withoutTagsText.replace('''&lt;Entity&gt;
#               &lt;ID&gt;0&lt;/ID&gt;
#               &lt;Start&gt;-1&lt;/Start&gt;
#               &lt;End&gt;-1&lt;/End&gt;
#               &lt;Rows&gt;
#                 &lt;string&gt;''', "")
    
#     withoutTagsText = withoutTagsText.replace('''&lt;/string&gt;
#               ...&lt;/Rows&gt;
#             ...&lt;/Entity&gt;''', "")
    
#     withoutTagsText = withoutTagsText.replace('''&gt;''', "")
    
#     withoutTagsText = withoutTagsText.replace('''...&lt;/''', "")
    
#     withoutTagsText = withoutTagsText.strip()
    
#     narratorsList = withoutTagsText.split("\n")
    
#     for i in range(len(narratorsList)):
#         narratorsList[i] = narratorsList[i].strip()
    
#     # End of code....
    
    
#     # Code for Book References....
#     flag = True
#     withoutTagsText = ""
#     for i in lists[3]:
#         if(i=="<"):
#             flag = False
#         if(flag):
#             withoutTagsText += i
#         if(i==">"):
#             flag=True
    
#     withoutTagsText = withoutTagsText.replace('''&lt;Entity&gt;
#               &lt;ID&gt;0&lt;/ID&gt;
#               &lt;Start&gt;-1&lt;/Start&gt;
#               &lt;End&gt;-1&lt;/End&gt;
#               &lt;Rows&gt;
#                 &lt;string&gt;''', "")
    
#     flag = True
#     count=0
#     refinedWithoutTagsText = ""
#     for i in withoutTagsText:
#         if(i=="'" and count==0):
#             count=1
#             flag = False
#         elif(i=="'" and count==1):
#             count=0
#             flag=True
#         if(flag):
#             refinedWithoutTagsText += i
    
    
#     refinedWithoutTagsText = refinedWithoutTagsText.replace('''&lt;/textref&gt;&lt;/conns&gt;&lt;/string&gt;
#               ...&lt;/Rows&gt;
#             ...&lt;/Entity&gt;
#             &lt;Entity&gt;
#               &lt;ID&gt;0&lt;/ID&gt;
#               &lt;Start&gt;-1&lt;/Start&gt;
#               &lt;End&gt;-1&lt;/End&gt;
#               &lt;Rows&gt;
#                 &lt;string/&gt;
#                 &lt;string/&gt;
#                 &lt;string&gt;&lt;conns&gt;&lt;textref reftype=' refid='&gt;''', "\n")
                
    
#     refinedWithoutTagsText = refinedWithoutTagsText.replace('''&lt;/textref&gt;&lt;/conns&gt;&lt;/string&gt;
#               ...&lt;/Rows&gt;
#             ...&lt;/Entity&gt;
#           ...&lt;/''', "\n")
    
#     lastIndex = refinedWithoutTagsText.rfind("&gt;")
    
#     refinedWithoutTagsText = refinedWithoutTagsText[lastIndex+4:-1]
    
#     refinedWithoutTagsText = refinedWithoutTagsText.strip()
    
#     bookReferencesList = refinedWithoutTagsText.split("\n")
    
#     for i in range(len(bookReferencesList)):
#         bookReferencesList[i] = bookReferencesList[i].strip()
     
#     # End of Code....
















          
          
          
          
          
          
          