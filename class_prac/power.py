class Power:
    def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x
        if x==-1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n < 0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x



print(Power().pow(5, 3))
print(Power().pow(1, 8))
print(Power().pow(10, 4))
print(Power().pow(0, 4))
print(Power().pow(10, 0))
print(Power().pow(5, -2))
