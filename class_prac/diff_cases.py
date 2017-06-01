class DifferentCases:
    def upper(self, sentence):
        return sentence.upper()
    def lower(self, sentence):
        return sentence.lower()
    def title(self, sentence):
        return sentence.title()

x = input("Enter a sentence or phrase: ")
print(DifferentCases().upper(x))
print(DifferentCases().lower(x))
print(DifferentCases().title(x))
