# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 11:54:36 2017

@author: OMNISLO
"""

counter = 0
bobcounter = 0


for x in s:
    if s[counter:counter+3]=='bob':
        bobcounter += 1
    counter += 1
        
print ('Number of times bob occurs is: ', str(bobcounter))
