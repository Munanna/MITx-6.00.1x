# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 11:54:17 2017

@author: OMNISLO
"""

counter = 0


for x in s:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        counter += 1
        
print ("Number of vowels: ", str(counter))
