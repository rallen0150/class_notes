
def sort_by_letter(sentence):
    words = sentence.split(' ')
    words.sort()
    sorted_words = ','.join(words)
    return sorted_words

sentence = input("Type in words seperated by spaces:\n").lower()
words = sort_by_letter(sentence)
print(words)
