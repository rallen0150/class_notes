# Make into Dictionary
def count_letters(words):
    number_letters = {}
    for x in words:
        letters = len(x)
        number_letters[x] = letters
    return number_letters


words = []
choice = ""
while choice != 's':
    choice = input("Would you like to (a)dd words to the word list or (s)top?\n>").lower()
    if choice == 'a':
        word = input("Type in the word:\n>")
        words.append(word)
        print(words)
    elif choice == 's':
        break
    else:
        print("Invalid Option")

word_list = count_letters(words)
print(word_list)
