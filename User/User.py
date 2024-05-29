# name: Tala khaled
# email: talakh1798@gmail.com
# desc:creating a class and making instances from it 
# ,accessing the methods and attributes of different instances

class user:
    def __init__(self,name,email_address,age):
        self.name=name
        self.email=email_address
        self.age=age
        self.account_balance=0
    def make_deposit(self,amount):
        self.account_balance+=amount    
    def make_withdrawal(self, amount):
        self.account_balance-=amount
    def  display_user_balance(self):
        print("user:",self.name," Balance:",self.account_balance)

user1=user("tala","talakh1798@gmail.com",26)
user2=user("khaled","khaled54@gmail.com",71)
user3=user("muhammad","muh.jj@yahoo.com",35)

print(user1.name,user1.email,user1.age)
print(user2.name,user2.email,user2.age)
print(user3.name,user3.email,user3.age)

user1.make_deposit(500)
user1.make_deposit(50)
user1.make_deposit(120)
user1.make_withdrawal(100)
user1.display_user_balance()

user2.make_deposit(100)
user2.make_deposit(1100)
user2.make_withdrawal(50)
user2.make_withdrawal(200)
user2.display_user_balance()

user3.make_deposit(1500)
user3.make_withdrawal(175)
user3.make_withdrawal(1000)
user3.make_withdrawal(150)
user3.display_user_balance()




