
def max_of_three(number):
    if number[0] > number[1] and number[0] > number[2]:
        max_num = number[0]
    elif number[0] < number[1] and number[1] > number[2]:
        max_num = number[1]
    else:
        max_num = number[2]
    return max_num

number = []
i = 1
for x in range(3):
    x = input("Enter number {} to find your max of three:\n>".format(i))
    number.append(x)
    i += 1

max_number = max_of_three(number)
print("The max number is {}".format(max_number))
