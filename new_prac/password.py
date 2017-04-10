from random import choice, randint
from string import ascii_letters, digits

password = ''

difficulty = input("How difficult do you want your password? Weak or Strong?\n>").lower()
if difficulty == 'weak' or difficulty == 'w':
    strength = randint(5, 12)
    for x in range(0, strength):
        password += choice(digits + ascii_letters)
elif difficulty == 'strong' or difficulty == 's':
    strength = randint(13, 25)
    for x in range(0, strength):
        password += choice(digits + ascii_letters)
print(password)
