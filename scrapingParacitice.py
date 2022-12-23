# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 02:20:38 2021

@author: iammu
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.rahimpardesi.com/collections/jackets'

page = requests.get(url)


soup = BeautifulSoup(page.text,'lxml')
#print(soup.find('div',{'class':'grid-product__price'}))
#print(soup.find('div',class_="grid-product__price"))

print(soup.find_all('div',{'class':'grid-product__price'})[1:])
