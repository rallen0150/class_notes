def sumOfTwo(a, b, v):
    yes = 0
    for x in range(0, len(a)):
        first = a[x]
        for y in range(0, len(b)):
            second = b[y]
            ans = first + second
            if ans == v:
                return True
    return False

a = [1, 2, 3]
b = [10, 20, 30, 40]
v = 42
print(sumOfTwo(a, b, v))
