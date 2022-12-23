@author: iammu
"""

import pandas as pd
from bs4 import BeautifulSoup
import mysql.connector
import requests
import re
myDb = mysql.connector.connect(host="localhost",user='root',passwd='*******',database='scholar_database')
myCursor = myDb.cursor()
query='select id from scholars;'

myCursor.execute(query)

result = myCursor.fetchall()

scholarIds=[]
for i in range(len(result)):
    scholarIds.append(result[i][0])

scholarIdList =[]
scholarParentsId =[]

for Id in scholarIds:

    url='https://muslimscholars.info/manage.php?submit=scholar&ID='+str(Id)
    page = requests.get(url)

    soup = BeautifulSoup(page.text,'lxml')
    table = soup.find('table',class_='form')
    
    
    tr = table.find_all('tr')
    
    td =  tr[3].find_all('td')
    
    if(td[0].text=="Parents:"):
        anchorTag = td[1].find_all('a')
        for a in  anchorTag:
            print("Found the URL:",Id, a['href'])
            aTag = a['href']
            scholarIdList.append(Id)
            scholarParentsId.append(aTag[29:])
            


data = pd.dataFrame()
data["Scholar_Id"] = scholarIdList
data["Parents_Id"] = scholarParentsId





