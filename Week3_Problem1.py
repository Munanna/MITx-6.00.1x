# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:51:46 2017

@author: OMNISLO
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'a', 'l', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))