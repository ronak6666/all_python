

class BankAccount:
    # don't forget to add some default values for these parameters!

    accounts = []
    def __init__(self, int_rate, balance): 
        self.interest_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        # print(self.balance)
        return self
        
        # your code here
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
        # your code here
    def display_account_info(self):
        print (f" Balance: {self.balance}")
        return self
        # your code here
    def yield_interest(self):
        self.balance = (self.balance * self.interest_rate) + self.balance
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate= 0.02, balance = 0)

    def make_deposits(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        return self 

    def display_balance (self):
        self.account.display_account_info()
        return self



user1 = User("ronak","ronp88@hotmail.com")
user1.make_deposits(20).make_withdraw(10).display_balance()


user2 = User("Rambo","rambo768@hotmail.com")
user2.make_deposits(50).make_withdraw(10).display_balance()

print(BankAccount.accounts)





# cookies = BankAccount(0.10, 10000000000 )
# (cookies.deposit(2).deposit(2).deposit(2).withdraw(2). yield_interest(). display_account_info())

# lookies = BankAccount(0.30, 20000000000 )
# (lookies.deposit(2).deposit(2).withdraw(2).withdraw(2).withdraw(2).withdraw(2).yield_interest(). display_account_info())

# chookies = BankAccount(0.40, 30000000000 )
# (chookies.deposit(600))





# when you do return statement make sure you don't do print statement of that method. That creates issues in the terminal. you have to have return statements for each terminal to do chaining. 


