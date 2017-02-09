def histogram(value):
    for x in value:
        graph = "*" * x
        print(graph)
    return "" # Returns nothing

numbers = []
x = input("How many values would you like to input?\n>")
x = int(x)

for n in range(x):
    value = input("Enter a number: ")
    value = int(value)
    numbers.append(value)

graph = histogram(numbers)
print(graph)
