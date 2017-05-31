# # This function finds the prime numbers
# class MyClass:
#
#     def init(self, num):
#         self.num = num
#
#     def isprime(self, startnumber):
#         self.startnumber = startnumber
#         startnumber*=1
#         for divisor in range(2,int(startnumber**0.5)+1):
#             if startnumber/divisor==int(startnumber/divisor):
#                 return False
#         return True
#
#     prime=[]
#
#     # Sets a limit for the maximum prime number
#     for a in range(2,100):
#         if MyClass.isprime(num):
#             prime.append(a)
#
#     print(prime)
#
# print(MyClass(20))
##########################################################

class MyClass:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        prime=[]
        # Sets a limit for the maximum prime number
        for a in range(2,self.num):
            if a > self.num:
                raise StopIteration
            elif self.isprime(a):
                prime.append(a)
        return prime
    def isprime(self, num):
        num = num
        num*=1
        for divisor in range(2,int(num**0.5)+1):
            if num/divisor==int(num/divisor):
                return False
        return True

x = int(input("Enter a max number to find the prime numbers up to your input: "))

for c in MyClass(x):
    print (c)
