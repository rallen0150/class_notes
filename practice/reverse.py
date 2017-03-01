def reverse(words):
    return ', '.join(reversed(words.split(',')))

words = input("Enter a list of words seperated by a comma:\n>")
print(reverse(words))
