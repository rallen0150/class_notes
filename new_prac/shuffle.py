from random import shuffle

sentence = input("Enter a word or phrase: ")
sentence = sentence.split()
bank = []

for x in range(count(sentence)):
    word = shuffle(sentence[x])
    bank.append(word)

sentence = ' '.join(bank)
print(sentence)
