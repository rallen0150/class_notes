from random import choice

num = int(input("What is your number?:\n>"))
print("I will have 25 guesses to get your number!")
comp_guess = choice(range(0, 100))

guess = 1
while comp_guess != num and guess <= 25:
    if comp_guess < num:
        print("My Guess: {}\nToo Low!".format(comp_guess))
        comp_guess = choice(range(comp_guess,100))
        guess+=1
    elif comp_guess > num:
        print("My Guess: {}\nToo High!".format(comp_guess))
        comp_guess = choice(range(0,comp_guess))
        guess+=1

if guess < 25:
    print("I beat you!!!\nAnd it took me {} tries".format(guess))
else:
    print("You beat me...")
