# Hangman
import random
import string

# integrate external word list
wordlist = open('read-write-folder/files-to-read/wortdatei.txt')
for line in wordlist:
    #print(line)
    word_list = [(line[])]
# print(wordlist.read())

print (word_list)
exit()


set_min = 1
set_max = len(word_list)

random_number = random.randint(set_min, set_max)
random_word = word_list[random_number - 1]
word_length = len(random_word)

print('Hey, you are welcome playing a round of hangman.\n'
      'A word with ' + str(word_length) + ' characters has been selected.')
game_mode = input('Do you want to play the "hard" or "easy" mode?\n').lower()

while game_mode != 'easy' and game_mode != 'hard':
    print('You have to choose a correct game mode:')
    game_mode = input('Do you choose "hard" or "easy" mode?\n').lower()

if game_mode == 'easy':
    number_of_guesses = 20
else:  # elif game_mode == 'hard':
    number_of_guesses = 10

print('In the ' + game_mode + ' Mode you have ' + str(
    number_of_guesses) + ' times to guess.\nOkay, let\'s get started! Good Luck to you.')

guess_left = number_of_guesses

# Abfrage eines Buchstabens (Single character, Only Letters)
while True:
    userInput = input('What\'s your guess?\n')
    if len(userInput) == 1:
        if userInput in string.ascii_letters:
            break
        print('Please enter only letters')
    else:
        print('Please enter only one character')
guessInUpper = userInput.upper()

# only if a Charakter is guessed, that the user has not guessed before
guess_left = guess_left - 1
guessed_word_complete = False
# correct_guessed_letter =

while guess_left > 0 or guessed_word_complete is True:
    if guessInUpper in random_word.upper():
        # correct_guessed_letter = correct_guessed_letter.append(guessInUpper)
        guess_left = guess_left - 1
        print('WOW ' + str(guess_left))  # correct_guessed_letter[0])

    else:
        # wrong_guessed_letter = [] + guessInUpper
        guess_left = guess_left - 1
        print('This Letter is not in the Word, you have ' + str(guess_left) + ' guesses left.')
