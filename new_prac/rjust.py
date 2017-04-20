n = int(input("Enter a number: ").strip())
for x in range(1, n+1):
    print(("#"*x).rjust(n))

for x in range(1, n+1):
    print(("*"*x).ljust(n))
