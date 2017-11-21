class Bank:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

a = Bank()
print(a.deposit(50))
print(a.deposit(25))
print(a.withdraw(40))
