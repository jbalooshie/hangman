import time
import random
# TODO: Add a wordbank that keeps track of your guesses. 
# TODO: Add handling for if you guess a word you have already guessed. 
# TODO: Add logic that allows you to guess with a capital or lowercase letter or word. 
# TODO: Refactor play_again() to have simpler logic. 

def greeting():
    print('Welcome to Hangman!')
    time.sleep(3)
    print('Get ready to play!')
    time.sleep(3)

def pick_word():
    word_file = open('words.txt', 'r')
    word_list = word_file.readlines()
    word = word_list[random.randrange(11117)].capitalize().strip()
    word_file.close()
    print('Choosing a word...')
    time.sleep(3)
    return word

def gameplay():
    print('You can guess by typing a letter. Or enter a whole word to try to solve the puzzle.')
    time.sleep(3)
    print('The game ends after 5 incorrect guesses.')
    time.sleep(3)
    word = pick_word()
    guessed_letters = ''
    print('Your word is:')
    time.sleep(3)
    current_hint = create_hint(word, guessed_letters)
    print(current_hint)
    time.sleep(3)
    guesses = 0
    while guesses < 5:
        print('You have ' + str(5 - guesses) + ' guesses remaining.')
        guess = input('Enter your guess:\n')
        if guess == word:
            print(f'Congratulations! You solved the puzzle with {guesses} remaining.')
            time.sleep(3)
            break
        elif guess in word:
            print('Correct!')
            guessed_letters = guessed_letters + guess
            time.sleep(1)
            print('Your word is:')
            time.sleep(1)
            current_hint = create_hint(word, guessed_letters)
            print(current_hint)
        else:
            print('Wrong!')
            guesses = guesses + 1
    if guesses == 5:
        print(f'Out of guesses! The word was {word}')

def create_hint(full_word, letters):
    hint = ''
    hint = hint + full_word[0]
    my_slice = full_word[1:]
    for x in my_slice:
        if x in letters:
            hint = hint + x
        else:
            hint = hint + '_'
    return hint

def play_again():
    response = input('Would you like to play again? Y/N\n').upper()
    if response == 'Y':
        return True
    elif response == 'N':
        print('Thanks for playing!')
        time.sleep(3)
        return False
    else:
        print('Invalid response, exiting...')
        time.sleep(3)
        return False

def menu():
    greeting()
    while True:
        gameplay()
        if not play_again():
            break


if __name__ == '__main__':
    menu()

