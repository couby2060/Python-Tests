import random

set_min = 1
set_max = 6

print('With how many dices do you want to play?')
number_of_dices = int(input())


def roll():
    print('Rolled the Dices and got a: ' + str(random.randint(set_min, set_max)))


n = 0
while n < number_of_dices:
    roll()
    n = n + 1
