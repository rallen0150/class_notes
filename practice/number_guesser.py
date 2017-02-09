from random import randint

# # This part works, but the while loop didn't until I did it this way
# def guess_age(guess):
#     your_guess = int(guess)
#     if your_guess < number:
#         answer = "I am not that Young!"
#     elif your_guess > number:
#         answer = "Wow, you think I'm that OLD?!?!?!"
#     else:
#         answer = "Amazing! You are correct!"
#
#     return answer


number = randint(1,100)
x = 0

while x < 10:
    guess = input("You have {} turns to guess the random number:\n>".format(10-x))
    guess = int(guess)
    if guess < number:
        print("Too Small!")
    elif guess > number:
        print("Too Big!")
    else:
        print("Amazing! You are correct!")
        break
    x += 1
if x == 10:
    print("You couldn't guess it in the alloted turns! The correct number is {}".format(number))
