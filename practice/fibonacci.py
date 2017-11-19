def fib(x):
    i = 1
    if x == 0:
        sequence = []
    elif x == 1:
        sequence = [1]
    elif x == 2:
        sequence = [1,1]
    else:
        sequence = [1,1]
        while i < (x-1):
            next_fib = sequence[i] + sequence[i-1]
            sequence.append(next_fib)
            i+=1
    return sequence

num = int(input("How many Fibonacci Numbers do you want?\n>"))
print(fib(num))
