# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 07:58:41 2019

@author: Jaesung
"""


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    get_guessed_word = " "
    for i in secret_word:
        if i in letters_guessed:
            get_guessed_word += i
        else:
            get_guessed_word += "_"
    return  get_guessed_word

secret_word = "apple"
letters_guessed = ['e','i','k','p','r','s']
print (get_guessed_word(secret_word, letters_guessed))