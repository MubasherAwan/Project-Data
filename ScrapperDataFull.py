# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 09:29:00 2022

@author: iammu
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Column=["Scholar","Scholar Type","Full Name","Parents","Siblings","Birth Date/Place","Death Date/Place","Places of Stay","Area of Interest","Spouse(s)","Children","Teachers/Narrated From","Students/Narrated By","Tags","Analysis","Brief Biography","Last Updated","References","Narrations(Unconfirmed)","Thadeeb al-Kamal","Other"]
Column=["Name","Name Type","Full Name"]
df = pd.DataFrame(columns = Column)

url='http://muslimscholars.info/manage.php?submit=scholar&ID=9989'
page = requests.get(url)
#print(page)
soup = BeautifulSoup(page.text,'lxml')
#print(soup)
table = soup.find('table',class_='form')
#print(table)

HeadingList=["Scholar:","Full Name:","Parents:","Siblings: ","Birth Date/Place: ","Death Date/Place: ","Places of Stay: ","Area of Interest:","Spouse(s):","Children :","Teachers/Narrated From:","Students/Narrated By:","Tags :","Analysis:","Brief Biography: ","Last Updated:","References:","Narrations:(Unconfirmed)","Thadeeb al-Kamal:"]


idCounter=9989
while idCounter<=9999:
    if not(table == None):
        Name=''
        Name_Type=''
        FullName=''
        # Parents=''
        # Siblings=''
        # BirthDatePlace=''
        # DeathDatePlace=''
        # PlacesofStay=''
        # AreaofInterest=''
        # Spouse=''
        # Children=''
        # TeachersNarratedFrom=''
        # StudentsNarratedBy=''
        # Tags=''
        # Analysis=''
        # BriefBiography=''
        # LastUpdated=''
        # References=''
        # NarrationsUnconfirmed=''
        # Thadeeb_al_Kamal=''
        # Other=''
            
        #tableRow = table.find_all('tr')
        tableRow = table.find_all('td')
        tableData=[]
        for i in range(len(tableRow)):
            td= tableRow[i].text
            tableData.append(td)
 
        
        DataList=[]
        for i in range(len(tableData)):
            if(tableData[i]=="Name:"):
                Scholar=tableData[i+1]
                Scholar_Type=tableData[i+2]
                # DataList.append(tableData[i+1])
                # DataList.append(tableData[i+2])
                
            elif(tableData[i]=="Full Name:"):
                #DataList.append(tableData[i+1])
                FullName=tableData[i+1]
                
            # elif(tableData[i]=="Parents:"):
            #     #DataList.append(tableData[i+1])
            #     Parents=tableData[i+1]
            #     tableData
            # elif(tableData[i]=="Siblings: "):
            #      #DataList.append(tableData[i+1])
            #      Siblings=tableData[i+1]
                
            # elif(tableData[i]=="Birth Date/Place: "):
            #     #DataList.append(tableData[i+1])
            #     BirthDatePlace=tableData[i+1]
            
                
            # elif(tableData[i]=="Death Date/Place: "):
            #     #DataList.append(tableData[i+1])
            #     DeathDatePlace=tableData[i+1]
            
            
            # elif(tableData[i]=="Places of Stay: "):
            #     #DataList.append(tableData[i+1])
            #     PlacesofStay=tableData[i+1]
            
                
            # elif(tableData[i]=="Area of Interest:"):
            #      #DataList.append(tableData[i+1])
            #      AreaofInterest =tableData[i+1]
            
                 
            # elif(tableData[i]=="Spouse(s):"):
            #     #DataList.append(tableData[i+1])
            #     Spouse=tableData[i+1]
            
                
            # elif(tableData[i]=="Children :"):
            #     #DataList.append(tableData[i+1])
            #     Children=tableData[i+1]
            
               
            # elif(tableData[i]=="Teachers/Narrated From:"):
            #     #DataList.append(tableData[i+1])
            #     TeachersNarratedFrom=tableData[i+1]
            
                
            # elif(tableData[i]=="Students/Narrated By:"):
            #     #DataList.append(tableData[i+1])
            #     StudentsNarratedBy=tableData[i+1]
           
                
            # elif(tableData[i]=="Tags :"):
            #     #DataList.append(tableData[i+1])
            #     Tags=tableData[i+1]
            
                
            # elif(tableData[i]=="Analysis:"):
            #     #DataList.append(tableData[i+1])
            #     Analysis=tableData[i+1]
                
                
            # elif(tableData[i]=="Brief Biography: "):
            #     #DataList.append(tableData[i+1])
            #     BriefBiography=tableData[i+1]
            
                
            # elif(tableData[i]=="Last Updated:"):
            #     #DataList.append(tableData[i+1])
            #     LastUpdated=tableData[i+1]
            
                
            # elif(tableData[i]=="References:"):
            #      #DataList.append(tableData[i+1])
            #      References=tableData[i+1]
            
                 
            # elif(tableData[i]=="Narrations:(Unconfirmed)"):
            #      #DataList.append(tableData[i+1])
            #      NarrationsUnconfirmed=tableData[i+1]
           
                 
            # elif(tableData[i]=="Thadeeb al-Kamal:"):
            #      #DataList.append(tableData[i+1])
            #      Thadeeb_al_Kamal=tableData[i+1]
                 
                 
        # if(tableData[-3] in HeadingList)==True:
        #     Other=tableData[-1]
        
        DataList.append(Scholar)
        DataList.append(Scholar_Type)
        DataList.append(FullName)
        # DataList.append(Parents)
        # DataList.append(Siblings)
        # DataList.append(BirthDatePlace)
        # DataList.append(DeathDatePlace)
        # DataList.append(PlacesofStay)
        # DataList.append(AreaofInterest)
        # DataList.append(Spouse)
        # DataList.append(Children)
        # DataList.append(TeachersNarratedFrom)
        # DataList.append(StudentsNarratedBy)
        # DataList.append(Tags)
        # DataList.append(Analysis)
        # DataList.append(BriefBiography)
        # DataList.append(LastUpdated)
        # DataList.append(References)
        # DataList.append(NarrationsUnconfirmed)
        # DataList.append(Thadeeb_al_Kamal)
        # DataList.append(Other)  
        
        
        length = len(df)
        df.loc[length]=DataList
        idCounter+=1  
        stringId=str(idCounter)
    else:
        idCounter+=1  
        stringId=str(idCounter)
    
    nextPage='http://muslimscholars.info/manage.php?submit=scholar&ID='+stringId
    page=requests.get(nextPage)
    soup=BeautifulSoup(page.text,'lxml')
    table = soup.find('table',class_='form')



# df.to_excel('FullData1.xlsx')   

#_____________________________Scrapping taqreeb ul thazeeb__________________________________



# from selenium  import webdriver
# from selenium.webdriver.common.keys import Keys
# import pandas as pd
# import time

# text=""

# driver = webdriver.Chrome('C:/Users/iammu/chromedriver.exe')
# # driver.get("https://shamela.ws/book/8609/3")
# # a=driver.find_elements_by_xpath('''//*[@id="wrapper"]/section[2]/div/div/div[2]/div[5]''')
# # for i in range(len(a)):
# #     text=text+a[i].text+"\n\n"
    

# for i in range(3,689):
#     driver.get("https://shamela.ws/book/8609/"+str(i))                                     
#     a=driver.find_elements_by_xpath('''//*[@id="wrapper"]/section[2]/div/div/div[2]/div[5]''')
    
#     for j in range(len(a)):
#         text=text+a[j].text+"\n\n\n\n"
#______________________________________________________________________________________



#_____________________________Scrapping tahzeeb ul thazeeb__________________________________



# from selenium  import webdriver
# from selenium.webdriver.common.keys import Keys
# import pandas as pd
# import time

# text=""

# driver = webdriver.Chrome('C:/Users/iammu/chromedriver.exe')
# for i in range(9,6394):
#     driver.get("https://shamela.ws/book/3310/"+str(i))   

                                  
#     a=driver.find_elements_by_xpath('''//*[@id="wrapper"]/section[2]/div/div/div[2]/div[5]''')
    
#     for j in range(len(a)):
#         text=text+a[j].text+"\n\n\n\n"
#______________________________________________________________________________________
        
        
        
            