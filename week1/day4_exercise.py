# input1 = "programming is fun"
# input2 = "i"
# output = [8, 12]

sentence = "i decided to learn how to program and it was a good decision"
letter = " "
output = []

# enumerate

for current_location, current_letter in enumerate(sentence):
    if current_letter == letter:
        output.append(current_location)

print(output)
