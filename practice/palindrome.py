
def palindrome(sentence):
    new_sentence = sentence
    new_sentence = new_sentence.replace(',', '').replace('.', '').replace("'" , "").replace('!', '').replace('"', '').replace('?',
    '').replace(':', '').replace(';', '').replace('&', '').replace(' ', '').lower()

    if new_sentence == new_sentence[::-1]:
        answer = "This IS a Palindrome!!!"
    else:
        answer = "Sorry, this is NOT a Palindrome!"

    return answer

sentence = input("Enter a word or phrase:\n>")
print(palindrome(sentence))
