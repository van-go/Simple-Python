# Design a single-player Hangman game using functions.
import random

# Welcome Screen & Get Username
# Get Word
# Play Game
# Play Again?


def welcome():
    # name = input("Welcome to the Hangman Game!"
    #              "Please enter your preferred game name: ")
    name = 'VanGo'
    print("Hi", name + '!',
          "The computer will randomly choose a word. "
          "You will try to guess what the word is. "
          "Good Luck, and have fun!")


def get_word():
    words = ['antelope', 'baboon', 'badger', 'battle', 'beard', 'beaver', 'camel', 'cattle', 'climb', 'cobra', 'cougar',
    'coyote', 'crowd', 'dirty', 'dodge', 'donkey', 'ducks', 'eagle', 'ferret', 'foxtrot', 'frost', 'gloat', 'goose',
    'hippo', 'lions', 'lizard', 'llama', 'moldy', 'monkey', 'moose', 'mouse', 'mules', 'newton', 'otter', 'octopus',
    'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'rampage', 'rattle', 'raven', 'rhino', 'salmon', 'seldom',
    'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swanky', 'tiger', 'total', 'trout', 'turkey',
    'turtle', 'weasel', 'whale', 'wolves', 'wombat', 'zebra']
    return random.choice(words).lower()


def display_board(word, letters_guessed):
    print('Guessed Letters: ', letters_guessed)

    blanks = '_' * len(word)
    for i in range(len(word)):  # Replace blanks with correctly guessed letters.
        if word[i] in letters_guessed:
            blanks = blanks[:i] + word[i] + blanks[i + 1:]

    for letter in blanks:  # Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    print()


def play_again():
    another_game = input("Would you like to play again? Enter Y for yes, N for no.").lower()
    if another_game == 'y':
        run_game()
    else:
        print('Hope you had fun playing!')


def run_game():
    welcome()
    word = get_word()

    tries = 7
    alphabet = ('abcefghijklmnopqrstuvwxyz')
    letters_guessed = []
    guessed = False

    print('The word contains', len(word), 'letters.')
    print(len(word) * '_ ')

    while guessed == False and tries > 0:
        print("=====================================================================")
        print('You have ' + str(tries) + ' tries remaining.')
        display_board(word, letters_guessed)
        guess = input("Enter a letter in the word, or the entire word: ").lower()
        if len(guess) == 1:
            if guess not in alphabet:
                print("Please guess a letter.")
            elif guess in letters_guessed:
                print("You have already guessed that letter. Try again.")
            elif guess not in word:
                print("Sorry, that letter is not in the word.")
                letters_guessed.append(guess)
                tries -= 1
            elif guess in word:
                print("Great! That letter is in the word")
                letters_guessed.append(guess)
        elif len(guess) > len(word):
            if guess == word:
                print("Great job. You guessed the word!")
                guessed = True
            else:
                print("Sorry, that was not the correct word")
                tries -= 1
        else:
            print("The length of your guess is not the same length as the word")

        status = ''
        for letter in word:
            if letter in letters_guessed:
                status += letter
        if status == word:
            guessed = True
            print('Great Job, you guess the word!\n')
            play_again()

    if tries == 0:
        print("The answer was ", word, '\n')
        play_again()


run_game()
