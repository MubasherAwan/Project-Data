# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:36:17 2021

@author: iammu
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url="http://muslimscholars.info/manage.php?submit=Find&scholarSearch=&ysource=0&tagSearch=&yfield=&ylist="

page = requests.get(url)


soup = BeautifulSoup(page.text,'lxml')
table = soup.find('table',class_='form')

headers=['Id','Scholar','Full Name/Scholar Type','Birth','Death','Interest','Resources','Notes']
df = pd.DataFrame(columns = headers)

tableRow = table.find_all('tr')
length=len(tableRow)
for i in range(length):
    td=tableRow[i].find_all('td')  
    rowDetail=[]  
    count=0
    for j in td:
        tlbdata=j.text
        if(count==0 or count==1 or count==2 or count==3 or count==4 or count==5 or count==6 or count==7):
            rowDetail.append(tlbdata)
        count+=1
    lengt=len(df)
    df.loc[lengt]=rowDetail

df

