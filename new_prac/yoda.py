from random import shuffle

sentence = input("Enter a phrase to have it rearranged like Yoda would say:\n")
sentence = sentence.split()
shuffle(sentence)
yoda = ' '.join(sentence)

print(yoda)
