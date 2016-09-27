print("Robbie" + " programs")

# print("Robbie" + 1) ERROR

class SuperNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return SuperNumber(str(self.value) + str(other.value))

    def __str__(self):
        return "DEBUG: Value is " + str(self.value)


s_number_1 = SuperNumber(1)
s_number_2 = SuperNumber("Robbie")

print(s_number_1)

x = s_number_1 + s_number_2 + s_number_2

print(x)
