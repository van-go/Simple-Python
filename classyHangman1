# Include underscores equivalent to the number of letters in the word.
# If a correct letter is entered, replace the underscore(s) with that letter.
# If a correct letter is not entered, the player gets one less attempt.
# A player is allowed up to 6 wrong guesses
# Allow selection of number of players
# Allow players to set their names
# Allow setting the number of guesses allowed
# Use a file for selection of a random word
import random


class Hangman:
    
    def __init__(self, word):
        """
        Initialize the game with a word to guess.
        :param word: word to guess
        """
        self.word = word.upper()
        self.guessed_list = []
        self.correct_letters = []
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.attempts = 7
        self.guessed = False
        print('There are ', len(self.word), 'letters in the word.')

    def display(self):
        print('Guessed letters: ', self.guessed_list)
        print('Number of guesses remaining: ', self.attempts)

        blanks = '_' * len(self.word)
        for char in range(len(self.word)):  # Replace blanks with correctly guessed letters.
            if self.word[char] in self.correct_letters:
                blanks = blanks[:char] + self.word[char] + blanks[char + 1:]
        for letter in blanks:  # Show the secret word with spaces in between each letter.
            print(letter, end=' ')
        print()

        user_input = input('Enter a letter: ')
        self.guessed_letter = user_input.upper()
        return self.guessed_letter

    def guess(self, guessed_letter):
        # print(self.word)
        if self.guessed is False and self.attempts > 0:
            if len(guessed_letter) == 1:
                if guessed_letter not in self.alphabet:
                    print('You did not enter a letter.')
                elif guessed_letter in self.guessed_list:
                    print('You already guessed that letter.')
                elif guessed_letter not in self.word:
                    print('That letter is not in the word.')
                    self.guessed_list.append(guessed_letter)
                    self.attempts -= 1
                elif guessed_letter in self.word:
                    self.correct_letters.append(guessed_letter)
                return self.attempts, self.guessed_list, self.correct_letters

        
def get_word():
    '''
    Selects a word from a list of words
    '''
    words = ['weather', 'amazing', 'balloon', 'jazzercise', 'ocarina']
    return random.choice(words)


def main():
    game = Hangman(get_word())
    result = game.display()
    res_gs = game.guess(result)
    while res_gs[0] > 0:
        result = game.display()
        res_gs = game.guess(result)
        
        
main()
