# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 08:16:11 2019

@author: Jaesung
"""

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    available_letters = string.ascii_lowercase
    get_available_letters = " "
    for i in available_letters:
        if i not in letters_guessed:
            get_available_letters += i
    return get_available_letters
    
letters_guessed = ['e', 'i', 'k', 'r', 's']
print(get_available_letters(letters_guessed) )