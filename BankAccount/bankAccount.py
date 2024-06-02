# name: Tala khaled
# email: talakh1798@gmail.com
# desc : Practice writing classes 

class BankAccount:
    def __init__(self, int_rate, Balance):
        self.int_rate = int_rate
        self.Balance = Balance
    
    def deposit(self, amount):
        self.Balance += amount
        return self
    
    def withdraw(self, amount):
        if amount < self.Balance:
            self.Balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")    
            self.Balance -= 5
        return self
    
    def display_account_info(self):
        print("Balance:", self.Balance)    
        return self 
    
    def yield_interest(self):
        if self.Balance > 0:
            self.Balance += self.Balance * self.int_rate 
        return self

account_user1 = BankAccount(0.07, 2000)
account_user2 = BankAccount(0.05, 1500)

account_user1.deposit(100).deposit(300).deposit(250).withdraw(450).yield_interest().display_account_info()
account_user2.deposit(200).deposit(300).withdraw(200).withdraw(50).withdraw(120).withdraw(70).yield_interest().display_account_info()

