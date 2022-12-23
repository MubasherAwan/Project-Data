# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:43:30 2022

@author: Ali Baqar
"""

from selenium import webdriver

pageList=[]


driver = webdriver.Chrome('C:/Users/Ali Baqar/chromedriver.exe')
for i in range(13070,23723,2):
    page=driver.get("https://www.ihsanetwork.org/HDBService.asmx/GetHadith2?textNum="+str(i)+"")
    htmlText=driver.find_element_by_class_name('pretty-print')


    pageText=htmlText.get_attribute('innerHTML')
    
    pageList.append(pageText)