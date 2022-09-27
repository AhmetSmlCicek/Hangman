
from typing import List, Union
import random


class Hangman():
    """ Hangman game class object to let users to play word guessing game. 
        Words to guess have been defines as class attributes."""

    possible_words = ['becode', 'learning', 'mathematics', 'session']

    def __init__(self):
        """" Class constructor where instance attributes have been defined.
             Each game starts with 5 lives and error and turn count get updated in their respective turn. """

        self.word_to_find = list(random.choice(Hangman.possible_words))
        self.well_guessed_letters: List[str] = ['_'] * len(self.word_to_find)
        self.badly_guessed_letters: List[str] = []
        self.lives = 5
        self.error_count = 0
        self.turn_count = 0

    def play(self):
        """Play method allows gamer to enter a letter and if the guessed letter is part of the word-to-find, 
           it will be added into well-guessed-letters list."""""

        self.entry = str(input('Enter a letter'))

        if self.entry.isalpha():
            if self.entry in self.word_to_find:
                # respective indexes of each letter in the word
                indexes = [i for i, x in enumerate(
                    self.word_to_find) if x == self.entry]
                for index in indexes:
                    # assign the same index as the letter has in its word
                    self.well_guessed_letters[index] = self.entry

            else:
                self.badly_guessed_letters.append(self.entry)
                self.error_count += 1
                self.lives -= 1
        else:
            # entry of other than letter will print this and ask user to enter again
            print('Please type a letter')
            self.play()

        self.turn_count += 1

    def start_game(self):
        """ This method starts the game. It checks for each turn if remaning lives is bigger than zero. 
            If so, it call play method and allows to enter a new letter. 
            If all the letters are found or no lives remaining it calls either well_played mor game_over """

        while self.lives > 0:
            self.play()
            print(f'Well guessed letters: {self.well_guessed_letters}')
            print(f'Badly guessed letters: {self.badly_guessed_letters}')
            print(f'Remaining lives: {self.lives}')
            print(f'Error count: {self.error_count}')
            print(f'Turn count: {self.turn_count}')
            if self.well_guessed_letters == self.word_to_find:
                self.well_played()
                break
        if self.lives == 0:
            self.game_over()

    def game_over(self):
        """ When all lives are lost, it will print game over """
        print('game over...')
        if self.lives == 0:
            input_user = input('Do you want to start over ? (Y/N)')
            if input_user == 'Y':
                self.__init__()
                self.start_game()
            else:
                print('see you again...')

    def well_played(self):
        """ If all letters of the word-to-find are guessed correctly, the use will see below message"""

        print(
            f'You found the word {self.word_to_find} in {self.turn_count} turns with { self.error_count} errors')
        if self.well_guessed_letters == self.word_to_find:
            input_user = input('Do you want to start over ? (Y/N)')
            if input_user == 'Y':
                self.__init__()
                self.start_game()
            else:
                print('see you again...')
