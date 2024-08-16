import time
import random

def greeting():
    print('Welcome to Hangman!')
    time.sleep(3)
    print('Get ready to play!')
    time.sleep(3)

def pick_word():
    word_file = open('words.txt', 'r')
    word_list = word_file.readlines()
    word = word_list[random.randrange(11117)].capitalize()
    word_file.close()
    print('Choosing a word...')
    time.sleep(3)
    return word

def gameplay(word):
    letters = []
    print(hint(letters, word))
    guess = input('You can guess by typing a letter. Or enter a whole word to try to solve the puzzle.\n')

def hint(letters, full_word):
    guessed_letters = []
    guessed_letters.append(full_word[0])
    guessed_letters.append('_' * (len(full_word) - 1))
    for x in letters:
        location = full_word.find(x)
        guessed_letters[location] = x
    return ''.join(guessed_letters)

def menu():
    greeting()
    gameplay(pick_word())

if __name__ == '__main__':
    menu()

