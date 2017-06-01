class Reverse:
    def reverse(self, string):
        return ' '.join(reversed(string.split(" ")))

sent = input("Enter a random sentence or saying: ")
print(Reverse().reverse(sent))
