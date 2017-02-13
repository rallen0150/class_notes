
# This function finds the prime numbers
def isprime(startnumber):
    startnumber*=1
    for divisor in range(2,int(startnumber**0.5)+1):
        if startnumber/divisor==int(startnumber/divisor):
            return False
    return True

prime=[]

# Sets a limit for the maximum prime number
for a in range(2,10001):
    if isprime(a):
        prime.append(a)

# print(prime)

add = []
next_prime = prime


# Adds up the all the prime numbers and finds the ones that add up to 10,000
for x in prime:
    # Sets a limit where no repeats of numbers are present
    if x < 5000:
        for i in next_prime[1:]:
            ans = x+i
            if ans == 10000:
                print('{} + {} = 10,000\n'.format(x, i))

# print(add)
