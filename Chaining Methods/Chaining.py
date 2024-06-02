# name: Tala khaled
# email: talakh1798@gmail.com
# desc:chain methods

class user:
    def __init__(self,name,email_address,age):
        self.name=name
        self.email=email_address
        self.age=age
        self.account_balance=0
    def make_deposit(self,amount):
        self.account_balance+=amount  
        return self  
    def make_withdrawal(self, amount):
        self.account_balance-=amount
        return self
    def  display_user_balance(self):
        print("user:",self.name," Balance:",self.account_balance)
        return self


user1=user("tala","talakh1798@gmail.com",26)
user2=user("khaled","khaled54@gmail.com",71)
user3=user("muhammad","muh.jj@yahoo.com",35)

user1.make_deposit(500).make_deposit(50).make_deposit(120).make_withdrawal(100).display_user_balance()
user2.make_deposit(100).make_deposit(1100).make_withdrawal(50).make_withdrawal(200).display_user_balance()
user3.make_deposit(1500).make_withdrawal(175).make_withdrawal(1000).make_withdrawal(150).display_user_balance()
