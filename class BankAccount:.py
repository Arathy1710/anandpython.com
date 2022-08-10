class BankAccount:
        def __init__(self):
            self.balance=0

        def withdraw(self,amount):
            self.balance-=amount
            return self.balance

        def deposit(self,amount):
            self.balance+=amount
            return self.balance
# a=BankAccount()
# b=BankAccount()
# print(a.deposit(100))
# print(b.deposit(50))
# print(b.withdraw(10))
# print(a.withdraw(10))
class MinimumBalanceAccount(BankAccount):
    def __init__(self,minimum_balance):
        super().__init__()
        self.minimum_balance=minimum_balance
        

    def withdraw(self,amount):
        if self.balance-amount<self.minimum_balance:
            print('sorry,minimum balance must be maintained.')
            return self.balance    
        else:
            super().withdraw(amount)
            return self.balance
           
a=MinimumBalanceAccount(200)
b=MinimumBalanceAccount(50)
print(1,a.deposit(100))
print(4,a.withdraw(10))
print(5,a.deposit(500))
print(8,a.withdraw(200))

        



                     