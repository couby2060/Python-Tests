# Dice Roller
# missing: function for setting up the number of dices

import random

set_min = 1
set_max = 6
roll_again = True
number_of_dices = 1

print('Program Roll the Dice started.')


# print('With how many dices do you want to play?')
# number_of_dices = input()

def roll():
    print('Rolled the Dices and got a: ' + str(random.randint(set_min, set_max)))
    print('Do you want to roll again?')


roll()
user_answer = input()

while roll_again:
    if user_answer == "yes":
        roll()
        user_answer = input()
        roll_again = True
    else:
        roll_again = False
        print('Program canceled')
