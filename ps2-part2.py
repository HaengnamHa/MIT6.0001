# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 08:30:48 2019

@author: Jaesung
"""

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


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
            get_guessed_word += "_ "
    return  get_guessed_word



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
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    letters_guessed = []
    warnings_remaining = 3
    guesses_remaining = 6
    vowel = ['a','e','i','o','u']
    unique_letters = []
    
    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters += letter
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word),"letters long.")
    print("You have 3 warnings left.")
    print("-" * 20)
    while True:
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter:" )
        if guess.isalpha()==False:
            warnings_remaining -= 1
            if warnings_remaining < 0:
                print("You have no warnings left so you lose one guess:", \
                      get_guessed_word(secret_word, letters_guessed))
                guesses_remaining -= 1
                continue
            print("Oops! That is not a valid letter. You have",  warnings_remaining,\
                "warnings_remaining:", get_guessed_word(secret_word, letters_guessed))
            print("-" * 20) 
            continue
        elif guesses_remaining < 1:
            print("Oops! That is not a valid letter. You have",get_guessed_word\
                  (secret_word, letters_guessed))
            print("-" * 20)
            print("Sorry, you ran out of guesses. The word was", secret_word)
            break
        else:
            guess = guess.lower()
            if guess in letters_guessed:
                warnings_remaining -= 1
                if warnings_remaining < 0:
                    print("You have no warnings left so you lose one guess:", \
                          get_guessed_word(secret_word, letters_guessed))
                    guesses_remaining -= 1
                    continue
                else:
                    print("Oops! You've already guessed that letter. You have",\
                          warnings_remaining, "warnings left.")
                    print(get_guessed_word(secret_word, letters_guessed))
                    print("-" * 20)
                    continue
            
            elif guess in secret_word and guess not in letters_guessed:
                                                   
                letters_guessed += guess
                print("Good guess: ",get_guessed_word(secret_word, letters_guessed))
                print("-" * 20)
                print( is_word_guessed(secret_word, letters_guessed))
                if is_word_guessed(secret_word, letters_guessed) == True:
                
                    print("Congratulations, you won!")
                    print("Your total score for this game is :", guesses_remaining\
                          * len(unique_letters))
                    break 
                else:
                    continue
            elif guess not in secret_word and guess in vowel:
                               
                guesses_remaining -= 2
                letters_guessed += guess
                
                if guesses_remaining < 1:
                    print("Oops!That letter is not in my word:", \
                          get_guessed_word(secret_word, letters_guessed) )
                    print("-" * 20)
                    print("Sorry, you ran out of guesses. The word was", secret_word)
                    break
                print("Oops!That letter is not in my word:", get_guessed_word\
                      (secret_word, letters_guessed) )
                print("-" * 20)
                continue
            
                           
            else:
                                            
                guesses_remaining -= 1
                letters_guessed += guess
                if guesses_remaining < 1:
                    print("Oops!That letter is not in my word:", get_guessed_word\
                          (secret_word, letters_guessed) )
                    print("-" * 20)
                    print("Sorry, you ran out of guesses. The word was", secret_word)
                    break
                print("Oops!That letter is not in my word:", get_guessed_word\
                      (secret_word, letters_guessed) )
                print("-" * 20)    
                
           
secret_word = "else"
hangman(secret_word)
            
                
                
                
                
                
                
                