def titlecase(sentence):
    return sentence.title()

sentence = titlecase("THIS IS A, SENTENCE")
print(sentence)

def title_case(sentence):
    newsentence = sentence
    prevchar = " "
    sentence1 = []
    for x in newsentence:
        if prevchar==" ":
            sentence1.append(x.upper())
        else:
            sentence1.append(x.lower())
        prevchar = x
    return ''.join(sentence1)

sentence = title_case("Hello World it is SO COOL!")
print(sentence)
