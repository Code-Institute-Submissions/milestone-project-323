import random
import time 

from hangmanwords import words_list

#variable for correctly guessed letters (global)
correct_guess_letter = []

#variable for incorrectly guessed letters (global)
incorrect_guess_letter = []

#variable for randomly chosen word (global)
random_chosen_words = ""

#variable for remaining lives left (global)
lives = 6

#variable for game over (global)
game_over = False


def random_word():
    #will return randomly chosen word for the hangman game
    pass

def word_before_guess():
    #this will print out dashes where the yet to be guessed letters of the word will be
    pass

def create_hangman():
    #will create a hangman in relation to how many lives are left of the player
    pass

def one_valid_letter():
    #makes sure that the player can only choose a letter that hasn't been chosen yet, and is a valid letter (i.e not a number or special case etc)
    pass

def guess_letter():
    #will check if the letter guessed is correct or wrong, and update the global variables accordingly
    pass

def game_over():
    #checks if the player has won or lost the game
    pass

def game_main():
    #the entry point of the game application, will call in all other mehtods for a game loop
    pass

if _name_ == '_main_':
    #will only be run if you run the game throguh the terminal or an IDE (like PyCharms)