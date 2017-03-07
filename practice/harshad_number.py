## Harshad's Number is an integer that is divisible by the sum of its digits (no decimal)
##   EXAMPLE: 81-> 8+1=9, 81/9=9

def harshad_num(x):
    nums = list(x)
    int_number = int(x)
    ans = 0
    for i in nums:
        i = int(i)
        ans += i

    if int_number%ans == 0:
        return ("This is a Harshad's Number!!!")
    return ("This is NOT a Harshad's Number...")

number = input("Enter a number: ")
y = harshad_num(number)
print(y)
