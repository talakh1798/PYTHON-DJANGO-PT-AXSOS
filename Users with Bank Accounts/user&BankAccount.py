# Name : tala khaled
# Email: talakh1798@gmail.com

class BankAccount:
    def __init__(self,int_rate,balance):
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
            return self

class user:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.account=BankAccount(int_rate=0.05,balance=0)

    def deposit(self,amount):
        self.account.deposit(amount)
        return self
    
    def withdraw(self,amount):
        self.account.withdraw(amount)
        return self
    
    def  display_user_balance(self):
        print("Name: {} ,Balance: {}".format(self.name , self.account.balance))
        # print(f"Name :{self.name} Balance:{self.account})

user1 = user("tala", "talakh1798@gmail.com")
user1.deposit(100)
user1.display_user_balance()