# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:41:06 2022

@author: iammu
"""

import requests
import pprint
import json
import time
from bs4 import BeautifulSoup

# txt='يوسف+ابن+عيسى+ابن+دينار+الزهري+أبو+يعقوب+المروزي+ثقة+فاضل+من+العاشرة+مات+سنة+تسع+وأربعين+خ+م+ت+س'
txt='''حدثنا أبو اليمان، قال أخبرنا شعيب، عن الزهري، قال أخبرني سالم بن عبد الله، أن عبد الله بن عمر، قال أخذ عمر جبة من إستبرق تباع في السوق، فأخذها فأتى رسول الله صلى الله عليه وسلم فقال يا رسول الله ابتع هذه تجمل بها للعيد والوفود‏.‏ فقال له رسول الله صلى الله عليه وسلم ‏"‏ إنما هذه لباس من لا خلاق له ‏"‏‏.‏ فلبث عمر ما شاء الله أن يلبث، ثم أرسل إليه رسول الله صلى الله عليه وسلم بجبة ديباج، فأقبل بها عمر، فأتى بها رسول الله صلى الله عليه وسلم فقال يا رسول الله إنك قلت ‏"‏ إنما هذه لباس من لا خلاق له ‏"‏‏.‏ وأرسلت إلى بهذه الجبة فقال له رسول الله صلى الله عليه وسلم ‏ تبيعها أو تصيب بها حاجتك'''
url='https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-mix-ner?text='+txt
#params={'text',txt}

# time.sleep()
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
print(soup)

Divv = soup.find('pre',class_='mt-3 max-h-screen overflow-auto text-xs text-gray-600 bg-gray-100 dark:bg-gray-800 p-2 rounded')

print(Divv)


if(response.status_code==200):
    data = json.loads(response.text)
    pprint.pprint(data)
else:
    print(f"Error: {response.status_code}")        