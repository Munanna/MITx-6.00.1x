# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 21:02:53 2017

@author: OMNISLO
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    availableLetters = "".join([letter for letter in string.ascii_lowercase if letter not in lettersGuessed])
    return availableLetters

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))