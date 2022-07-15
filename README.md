---Hangman Rules---
1. Once every game a random word will be chosen from the list in words.py
2. The player will have a total of 6 lives, if the player chooses 6 incorrect letters he/she/they will lose.
3. Only one letter can be guessed at a time
4. The letter that has been previously guessed incorrectly will be shown to the player so as not to be chosen again by mistake.
5. Before every guess the player will be shown a hangman to help keep the player on track with how many lives are left.
6. If all the letters were correctly guessed by the player before his/hers/their lives run out the player will win the game, which
    will be shown on screen.
7. If all lives has been lost, the hangman drawing will be completed and the player has lost. A message will display on screen
    telling the player of his/her/their loss.

problems yet to be solved:
    1. pylint (missing-function-docstring)

problems and their solutions
    1. changing the range and len method to a enumerate method.