scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

letters = input("What are the letters in your rack? Seperate by spaces:\n>")
letters = letters.split(' ')

matches = []

def wordscore(word):
    total = 0
    for letter in word:
        total += scores[letter]
    return total

def index(listhere, var):
    return [i for i,n in enumerate(listhere) if n == var]

def allletters(word):
    for letter in word:
        if len(index(word, letter)) > len(index(letters, letter)):
            return False
        if letter not in letters:
            return False
    return True

with open('/usr/share/dict/words') as words:
    for word in words:
        word = word.strip()
        #if len(word) == requiredlen:
        if allletters(word):
            matches.append(word)
    print("Matches --> Score")

for match in matches:
    print(match, "-->", wordscore(match))
