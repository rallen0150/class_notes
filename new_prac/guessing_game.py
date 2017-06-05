from random import choice

number = choice(range(0, 100))
response = int(input("The number I have thought is between 1-100.\nEnter your Guess:\n>"))
count = 1

while response != number:
    if response < number:
        print("Too Low!")
    else:
        print("Too High!")
    response = int(input("Guess Again:\n>"))
    count += 1
print("CORRECT!!! It took {} tries to get it!".format(count))
