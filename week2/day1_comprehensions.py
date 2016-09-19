list_of_numbers = [9, 10, 5, 100, 23, 2]

half_values = []

for x in list_of_numbers:
    half_of_x = x / 2
    half_values.append(half_of_x)

print(half_values)

###############################################################

list_of_numbers = [22, 4, 65, 1, 2, 1]

half_values = [number / 2 for number in list_of_numbers]
print(half_values)

###############################################################

list_of_numbers = [100, 67, 23, 45, 11]

square_numbers = {}

for number in list_of_numbers:
    square_numbers[number] = number ** 2
    # ** # is how you do exponent

print(square_numbers)

###############################################################
# Dict comprehension way of the above

list_of_numbers = [100, 67, 23, 45, 11]

square_numbers = {number: number ** 2
                  for number in list_of_numbers}

print(square_numbers)

################################################################
# Nested comprehension

matrix = [["-", "X", "-"],
          ["O", "X", "O"],
          ["O", "X", "O"]]

target_column = []

for row in matrix:
    target_column.append(row[1])
print(target_column)

################################################################

matrix = [["-", "X", "-"],
          ["O", "X", "O"],
          ["O", "X", "O"]]

target_column = [row[1] for row in matrix]
print(target_column)
