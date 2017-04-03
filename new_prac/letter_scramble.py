from random import shuffle

def scramble_letters(word):
    word = list(word)
    shuffle(word)
    word = ''.join(word)
    return word

def scramble_sentence(sentence):
    sentence = sentence.split()
    new_sent = []
    for x in range(0, len(sentence)):
        word = sentence[x]
        word = scramble_letters(word)
        new_sent.append(word)
    new_sent = ' '.join(new_sent)
    return new_sent

sentence = input("Enter a phrase (Please no punctuation):\n")
print(scramble_sentence(sentence))
