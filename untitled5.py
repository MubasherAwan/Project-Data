# -*- coding: utf-8 -*-
"""
Created on Tue May 31 22:43:37 2022

@author: iammu
"""

#Saves the input as the variable 'mood'#
text_file = open("MoodDiary.txt", "w")
#Opens or creates the .txt file, sharing the directory of the script#
text_file.write(mood)
#Writes the variable into the .txt file#
text_file.close()
#Closes the .txt file#