# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:13:13 2021

@author: iammu
"""

import requests
from bs4 import BeautifulSoup

url='https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)

#print(page.text)

soup = BeautifulSoup(page.text,'lxml')
print(soup)

name = soup.find_all('a',class_='title')
nameList=[]
for i in name:
    N = i.text
    nameList.append(N)
    
price = soup.find_all('h4',class_='pull-right price')
priceList=[]

for i in price:
    H = i.text
    priceList.append(H)