# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate in decimal format. For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)
# The class should also have the following methods:
# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
# Create 2 accounts
# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info

all_accounts = []
class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, name, int_rate=0.01, balance=0):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        all_accounts.append(name)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        # your code here
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        else:
            self.balance = self.balance - amount
        return self
    def display_account_info(self):
        print(f"Balance = ${self.balance}")
        print(f"Interest Rate = {self.int_rate}")
        return self
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance = self.balance * (1+self.int_rate)
        return self
    def print_accounts(self):
        # print(all_accounts)
        return all_accounts
    

acct_1 = BankAccount(name="acct_1", int_rate=.02)
acct_2 = BankAccount(name="acct_2", balance=100)
acct_1.deposit(10).deposit(20).deposit(60).withdraw(50)
acct_2.deposit(200).deposit(30).withdraw(5).withdraw(10).withdraw(5).withdraw(10).yield_interest().display_account_info()
print(acct_1.display_account_info())
print(acct_2.print_accounts())