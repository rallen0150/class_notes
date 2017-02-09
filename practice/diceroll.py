from random import randint

def options(choice):
    if choice == 'r':
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        dice_sum = dice1 + dice2
        return "Dice 1: {}\nDice 2: {}\nSum of Dice: {}".format(dice1, dice2, dice_sum)
    elif choice == 'q':
        return "Have a great rest of the day!"
    else:
        return "Invalid Choice"

choice = ""
while choice != 'q':
    choice = input("Would you like to (r)oll the dice or (q)uit?\n>").lower()
    turn = options(choice)
    print(turn)
