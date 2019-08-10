# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 07:46:14 2019

@author: Jaesung
"""


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word:
        if i not in letters_guessed:
            return False
        return True
    
secret_word = "apple"
letters_guessed = ['e', 'i', 'k', 'p','r','s']
print(is_word_guessed(secret_word, letters_guessed))
