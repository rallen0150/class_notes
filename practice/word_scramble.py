from random import choice, shuffle
from string import ascii_lowercase

open_file = open("/usr/share/dict/words")
words = open_file.read().lower()
open_file.close()

word = words.split('\n') # NEED THIS TO GET THE FULL WORD!!!

random_word = choice(word)
x = list(random_word)
shuffle(x)
scrambled_word = ''.join(x)

counter = 0
guess = ""

print("Guess the correct word in 5 tries from this scramble: {}".format(scrambled_word))

while guess != random_word and counter < 5:
    guess = input("What is the correct word?\n>").lower()
    counter += 1

if guess == random_word:
    print("CORRECT!!! The word was {}. It took {} tries to guess it!".format(random_word, counter))
else:
    print("Sorry, you couldn't guess it. The word was {}".format(random_word))
