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
is_game_over = False

#will return randomly chosen word for the hangman game
def random_word():
    global random_chosen_words

    #this is used as computers don't have any true randomness to them
    random.seed(time.time())
    #this will make the program choose a word from this list of 'acceptable words'
    random_chosen_words = random.choice(words_list)
    #this will make the randomly chosen word appear in uppercase (this will help with comparisons later on)
    random_chosen_words = random_chosen_words.upper()

#this will print out dashes where the yet to be guessed letters of the word will be
def word_before_guess():
    global correct_guess_letter
    global random_chosen_words

    for i in range(0, len(random_chosen_words)):
        letter = random_chosen_words[i]
        #print the correctly guessed letter
        if letter in correct_guess_letter:
            print(letter, end=" ")
        #print an a dash for the yet to be guessed letters
        else:
            print("_", end=" ")
    print("")

#will create a hangman in relation to how many lives are left of the player
def create_hangman():
    global lives

    if lives == 6:
        print("+-------------+")
        print("I             I")
        print("I")
        print("I")
        print("I")
        print("I")
        print("I")
        print("I")
        print("+-------+")
    elif lives == 5:
        print("+-------------+")
        print("I             I")
        print("I             O")
        print("I")
        print("I")
        print("I")
        print("I")
        print("I")
        print("+-------+") 
    elif lives == 4:
        print("+-------------+")
        print("I             I")
        print("I             O")
        print("I             I")
        print("I")
        print("I")
        print("I")
        print("I")
        print("+-------+") 
    elif lives == 3:
        print("+-------------+")
        print("I             I")
        print("I             O")
        print("I             I--")
        print("I")
        print("I")
        print("I")
        print("I")
        print("+-------+") 
    elif lives == 2:
        print("+-------------+")
        print("I             I")
        print("I             O")
        print("I           --I--")
        print("I")
        print("I")
        print("I")
        print("I")
        print("+-------+") 
    elif lives == 1:
        print("+-------------+")
        print("I             I")
        print("I             O")
        print("I           --I--")
        print("I             I")
        print("I            /")
        print("I")
        print("I")
        print("+-------+") 
    elif lives == 0:
        print("#-------------")
        print("I             I")
        print("I             O")
        print("I           --I--")
        print("I             I")
        print("I            / \\")
        print("I")
        print("I")
        print("#-------#") 

#makes sure that the player can only choose a letter that hasn't been chosen yet, and is a valid letter (i.e not a number or special case etc)
def one_valid_letter():
    is_letter_valid = False
    letter = ""
    while is_letter_valid is False:
        letter = input("Enter guess letter: ")
        letter = letter.strip().lower()
        #the letter can not be less than 1 or more than one (an input of 0 is invalid, so is an input of 2 and above!)
        if len(letter) <= 0 or len(letter) > 1:
            print("Invalid, letter has to be the length of 1")
        #the letter will be a letter from A-Z (no comma or number!)
        elif letter.isalpha():
            #if the letter has been chosen before it cannot be chosen again
            if letter in correct_guess_letter or letter in incorrect_guess_letter:
                print("You have already guessed this letter" + letter + "Please try again!")
            #if the letter passes every criteria above it will exit the negative feedback loop and stand as valid
            else:
                is_letter_valid = True
        else:
            #an error message if the letter chosen is not a letter from a-z
            print("letter must be from a-z")
    
    return letter

#will check if the letter guessed is correct or wrong, and update the global variables accordingly
def guess_letter():
    global correct_guess_letter
    global incorrect_guess_letter
    global lives

    letter = one_valid_letter()
    #if the guessed letter is in the randomly chosen word, append the letter to correct_guess_letter
    if letter in random_chosen_words:
        correct_guess_letter.append(letter)
    else:
        #if the the chosen word is incorrect remove one life and append to the incorrect_guessed_letter
        incorrect_guess_letter.append(letter)
        lives -= 1

#checks if the player has won or lost the game
def check_game_over():
    global lives
    global is_game_over
    global correct_guess_letter

    #if the lives left are less than or equal to 0 then game over is true and the hangman will be drawn
    if lives <= 0:
        is_game_over = True
        create_hangman()
        print("You have lost! The correct word was" + random_chosen_words + ". Better luck next time!")
    else:
        all_letters_correct = True
        for letter in random_chosen_words:
            #if all_letters_correct is false then it will break out of the positive feedback loop and check the next segment
            if letter not in correct_guess_letter:
                all_letters_correct = False
                break
        #if all the letters are correct and there are no more letters to guess then a message will display showing that you have won the game
        if all_letters_correct:
            is_game_over = True
            print("You have won the game! Congratulations! Feel free to try again!")

#the entry point of the game application, will call in all other mehtods for a game loop
def game_main():
    global is_game_over

    print("!WELCOME TO HANGMAN!")
    random_word()

    while is_game_over is False:
        create_hangman()
        word_before_guess()

        if len(incorrect_guess_letter) > 0:
            print("Incorrect guesses: ")
            print(incorrect_guess_letter)
    
        guess_letter()
        check_game_over()

#will only be run if you run the game throguh the terminal or an IDE (like PyCharms)
if __name__ == '__game_main__':