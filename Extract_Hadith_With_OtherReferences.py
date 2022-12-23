# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 19:09:23 2022

@author: iammu
"""

from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome('C:/Users/iammu/chromedriver.exe')
driver.get("https://www.ihsanetwork.org/hadith.aspx#")

x=driver.find_elements('''//*[@id="dijit_layout_ContentPane_27"]''')

    