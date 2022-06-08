class BankAccount:
    # don't forget to add some default values for these parameters!# your code here! (remember, this is where we specify the attributes for our class)
    def __init__(self, int_rate=0.0, balance=0.0):
        self.int_rate = int_rate
        self.balance = balance

    # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        self.balance -= amount
        return self

    def display_account_info(self):
        # your code here
        print(f"Name:{self.name}\nAccount Balance:${self.account_balance}\n")
        return self

    def yield_interest(self):
        # your code herecopy
        # if self.balance > 0:
        self.balance = self.balance * (1 + self.int_rate / 100)
        return self


class User:
    def __init__(self, name, email, account_balance=0):
        pass
        self.name = name
        self.email = email
        self.account_balance = account_balance
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_withdrawal(self, amount):
        self.account_balance -= amount

        return self

    def display_user_balance(self):
        print(f"Name:{self.name}\nAccount Balance:${self.account_balance}\n")

    def make_deposit(self, amount):
        self.account_balance += amount

        return self

    def transfer_money(self, user, amount):
        self.account_balance -= amount
        user.account_balance += amount
        return self


nora = User("nora", 'nora@python.com', 5000)
Sara = User("sara", 'sara@python.com', 6000)

Sara.make_deposit(400).make_deposit(20).make_deposit(
    10).make_withdrawal(700).account.yield_interest()
print(Sara.display_user_balance())

nora.make_deposit(400).make_deposit(
    20).make_withdrawal(400).make_withdrawal(80).make_withdrawal(200).make_withdrawal(40).account.yield_interest()
print(nora.display_user_balance())
