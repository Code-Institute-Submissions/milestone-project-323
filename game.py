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

#will return randomly chosen word for the hangman game
def random_word():
    global random_chosen_words

    #this is used as computers don't have any true randomness to them
    random.seed(time.time())
    random_chosen_words = random.choice(words_list)
    random_chosen_words = random_chosen_words.upper()

#this will print out dashes where the yet to be guessed letters of the word will be
def word_before_guess():
    pass

#will create a hangman in relation to how many lives are left of the player
def create_hangman():
    pass

#makes sure that the player can only choose a letter that hasn't been chosen yet, and is a valid letter (i.e not a number or special case etc)
def one_valid_letter():
    pass

#will check if the letter guessed is correct or wrong, and update the global variables accordingly
def guess_letter():
    pass

#checks if the player has won or lost the game
def game_over():
    pass

#the entry point of the game application, will call in all other mehtods for a game loop
def game_main():
    pass

#will only be run if you run the game throguh the terminal or an IDE (like PyCharms)
if _name_ == '_main_':