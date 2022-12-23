# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:30:42 2022

@author: iammu
"""

from camel_tools.ner import NERecognizer
from camel_tools.tokenizers.word import simple_word_tokenize
ner = NERecognizer('CAMeL-Lab/bert-base-arabic-camelbert-msa-ner')
sentence = simple_word_tokenize('يحيى بن بكير')
ner.predict_sentence(sentence)




from transformers import pipeline
ner = pipeline('ner', model='CAMeL-Lab/bert-base-arabic-camelbert-msa-ner')
ner("إمارة أبوظبي هي إحدى إمارات دولة الإمارات العربية المتحدة السبع")