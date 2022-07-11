    #variable for correctly guessed letters
    #variable for incorrectly guessed letters
    #variable for randomly chosen word
    #variable for remaining lives left
    #variable for game over

def random_word():
    #will return randomly chosen word for the hangman game

def word_before_guess():
    #this will print out dashes where the yet to be guessed letters of the word will be

def create_hangman():
    #will create a hangman in relation to how many lives are left of the player

def one_valid_letter():
    #makes sure that the player can only choose a letter that hasn't been chosen yet, and is a valid letter (i.e not a number or special case etc)

def guess_letter():
    #will check if the letter guessed is correct or wrong, and update the global variables accordingly

def game_over():
    #checks if the player has won or lost the game

def game_main():
    #the entry point of the game application, will call in all other mehtods for a game loop