def factorial(x):
    original = x
    x += 1
    ans = 1
    for i in range(1, x):
        ans *= i
    return ("The factorial of {} is {}".format(original, ans))

number = input("Enter the number you want to find the factorial: ")
number = int(number)
print(factorial(number))
