# class based game
import random


def begin_end(func):                            # a decorator that prints before and after a function
    def wrapper(*args, **kwargs):
        print(" Welcome to Hangman")
        func(*args, **kwargs)
        print("Thanks for playing!")
    return wrapper


class Hangman:
    def __init__(self):                         # runs automatically whenever a game instance is created
        self.guessed = []
        self.guess = ''
        self.result = ''
        self.players = []
        self.random_word = ''
        self.finished = False

    def add_player(self, name):                 # appends names of players in game to a list
        self.players.append(name)

    def get_word(self):                         # randomly chooses a word from given file
        f = open('words.txt', 'r')
        words = f.read().split()
        self.random_word = random.choice(words).upper()

    def take_turn(self, name):
        self.guess = (input("\n\nPlease input a letter between A-Z or the correct word" + "\n> ")).upper()
        if len(self.guess) > 1:                 # if 1+ letter entered, it is assumed it is a word

            if self.guess == self.random_word:  # if word input is correct,
                self.finished = True            # finished = true, we do not return to
                print(name + ", You Win!")      # while loop. Player wins
            return True                         # turn = true
        else:
            if not self.guess.isalpha():        # checks to ensure input is a letter. If not,
                print("That is not a letter. Try again.")  # turn = false and user is asked
                return False                    # to put input again

            if self.guess in self.guessed:      # checks that the letter has not been guess already
                print("You already guessed that letter. Try again")  # If not, turn = False and
                return False                    # user is asked to put input again

            self.guessed += self.guess          # if input is valid, it is added to guessed list

            # if all the guessed letters match the random word, finished = True and player wins
            self.finished = all([char in self.guessed for char in self.random_word])

            return True         # turn = true and moves to next player

    @begin_end                  # the wrapper text will appear at the beginning and end of method
    def play(self):
        while self.finished is False:
            for i in (self.players):
                print("******************************")  # prints out the player name and guessed
                print(i + ", it is your turn.")          # letters
                print("\nLetters Guessed: %s" % self.guessed)
                print("\n")

                blanks = '_' * len(self.random_word)
                for char in range(len(self.random_word)):  # Replace blanks with correctly guessed letters.
                    if self.random_word[char] in self.guessed:
                        blanks = blanks[:char] + self.random_word[char] + blanks[char + 1:]

                for letter in blanks:  # Show the secret word with spaces in between each letter.
                    print(letter, end=' ')
                print()

                turn = self.take_turn(i)        # name is given to the take_turn method and method is called

                while not turn:                 # while turn = False, the same player is
                    turn = self.take_turn(i)    # is guessing a letter

                if self.finished is True:       # if the player correctly guesses the word
                    print("\n" + i + ", You Win!")   # they win
                    break                       # end the game


class PreSetHangman(Hangman):
        def get_word(self):
            self.random_word = 'HOSPITAL'

game = PreSetHangman()

num_players = int(input("\nEnter the number of players: " + "\n>"))
for i in range(num_players):
    player_name = input("\nEnter player name: ")
    game.add_player(player_name)

word = game.get_word()
game.play()
