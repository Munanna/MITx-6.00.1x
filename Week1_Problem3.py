# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 01:59:39 2017

@author: OMNISLO
"""
import string
alphabet = string.ascii_lowercase

ind=[]
counter = 0
for x in s:
    ind.append(alphabet.index(s[counter]))
    counter += 1


counter = 0
alphabetical_strings = ''
nxt = ''
for x in ind:
    while counter+1 <= (len(ind)-1):
        if (ind[counter] <= ind[counter+1]):
            alphabetical_strings += s[counter]
            nxt = s[counter+1]
            #print (next)
        else:
            alphabetical_strings += str(nxt)
            alphabetical_strings += ','
            nxt = s[counter]
        counter += 1
alphabetical_strings += str(nxt)

strings = alphabetical_strings.split(',')

print ('Longest substring in alphabetical order is: '+max(strings,key=len))

