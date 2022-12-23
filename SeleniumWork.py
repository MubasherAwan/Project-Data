# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:04:36 2022

@author: iammu
"""

from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

finallist=[]
driver = webdriver.Chrome('C:/Users/iammu/chromedriver.exe')
   
for i in  range(1,5):
    driver.get("https://shamela.ws/book/8609/4")
    #x=driver.find_elements_by_xpath('''//*[@id="wrapper"]/section[2]/div/div/div[2]/div[5]''')
    x=driver.find_elements('''//*[@id="wrapper"]/section[2]/div/div/div[2]/div[5]''')
    for i in range(len(x)):
        #finallist=finallist+mylist
        # dum=x[i].text
        # mylist.append(dum)
        # dum=''
        print(x[i].text)
    
# txt='يوسف+ابن+عيسى+ابن+دينار+الزهري+أبو+يعقوب+المروزي+ثقة+فاضل+من+العاشرة+مات+سنة+تسع+وأربعين+خ+م+ت+س'
# for i in range(len(li)):
#     driver.get('https://muslimscholars.info/manage.php?submit=scholar&ID=')
    
#     driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[1]/th/font').text


# '//*[@id="product-search-results"]/div[2]/div[2]/div/div/div[1]/div/div/a/div[2]/div[1]/div/span/span'

# box=driver.find_element_by_xpath('/html/body/div/main/div/section[2]/div[3]/div/div/form/label/span')

# box.send_keys("يوسف ابن عيسى ابن دينار الزهري أبو يعقوب المروزي ثقة فاضل من العاشرة مات سنة تسع وأربعين خ م ت س")

# button = driver.find_element_by_xpath('/html/body/div/main/div/section[2]/div[3]/div/div/form/button')
# button.click()



# button1 = driver.find_element_by_xpath('/html/body/div/main/div/section[2]/div[3]/div/div/div[5]/button[1]')
# button1.click()


# import pandas as pd

# #testdata = pd.read_excel("TeacherStudentV3.xlsx")

# data=pd.read_excel("ScholarName.xlsx")
# data2=pd.read_excel("ScholarArabicNames.xlsx")


# df=pd.DataFrame(columns=["arabic_names"])





# x=data2["arabic_names"].values
# x=list(x)


# x=x[2485:]

# x_axis=data["Scholar"].values
# x_axis=list(x_axis)


# y_axis=data["Scholar"].values
# y_axis=list(y_axis)


# li=[]
# lis=[]
# for i in range(len(arabicList)):
#     if(i in li):
#         lis.append(y_axis[i])


# arabicList=[]
# arabicList2=[]
# arabicListTest=arabicList
# driver.get('https://www.google.com/search?q=google+translate+english+to+arabic&rlz=1C1BNSD_enPK976PK976&oq=google+translate+english+to+a&aqs=chrome.1.69i57j0i512l4j0i20i263i512j0i512j69i61.13417j1j7&sourceid=chrome&ie=UTF-8')
# for i in range(len(lis)):    
#     # englishBox=driver.find_element_by_xpath('//*[@id="tw-cst"]/span/svg/path').click()
#     englishBox=driver.find_element_by_xpath('//*[@id="tw-source-text-ta"]')
#     englishBox.send_keys(lis[i])
#     time.sleep(3)
#     arBox=driver.find_elements_by_xpath('//*[@id="tw-target-text"]/span')
#     temp=arBox[0].text
#     arabicList2.append(temp)
#     #time.sleep(1)
    
#     driver.find_element_by_xpath('//*[@id="tw-cst"]').click()
    
#     temp=''

    
# print(arabicList[183181])


# for i in range(len(x)):
#     arabicList.append(x[i])

# li=[]
# lis=[]
# for i in range(len(arabicList)):
#     if(i in li):
#         lis.append(y_axis[i])
# #_______________________________________________________________________________
# # Translating...  
# #(بلا هوية)
# count=0
# for i in range(len(arabicList)):
#     if(str(arabicList[i])=='nan'):
#         # lis.append(y_axis[i])
#         arabicListTest[i]=arabicList2[count]
#         count=count+1

# arabicList[25243]="محمد ب. صالح العثيمين أبو عبد الله"


# df["arabic_names"]=arabicList

# df.to_excel("Arbic_Names.xlsx")

#___________________________________________________________________________
import requests
from bs4 import BeautifulSoup
import pandas as pd
mylist=[] 


ddat=pd.read_excel("C:/Users/iammu/Book_96955.xlsx")
mylist=list(ddat["book96955"])

for i in range(2079,6010):
    url='https://shamela.ws/book/96955/'+str(i)
    page = requests.get(url)
    #print(page)
    soup = BeautifulSoup(page.text,'lxml')
    #print(soup)
    table = soup.find('div',class_='nass margin-top-10')
    #print(table)
    
    p=table.find_all('p')
    for i in range(len(p)):
        print(p[i].text)
        mylist.append(p[i].text)


df = pd.DataFrame()

df["book96955"]=mylist

df.to_excel("Book_96955.xlsx")

#_______xml to txt____________

listTxt = list(df['Meezan ul Aitedal'])

Docfile=""
for i in range(len(listTxt)):
    Docfile=Docfile + listTxt[i]
    
    
    
text_file = open("C:/Users/iammu/OneDrive/Desktop/Text.txt", "w",encoding='utf-8')
#Opens or creates the .txt file, sharing the directory of the script#
text_file.write(Docfile)
#Writes the variable into the .txt file#
text_file.close()


