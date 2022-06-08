
class BankAccount:
    # don't forget to add some default values for these parameters!# your code here! (remember, this is where we specify the attributes for our class)
    def __init__(self, int_rate=0.02, balance=0.0):
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
        print(
            f"Account Balance:${self.account_balance}\n rate:{self.int_rate}\n")
        return self

    def yield_interest(self):
        # your code herecopy
        # if self.balance > 0:
        self.balance = self.balance * (1 + self.int_rate / 100)

        return self


nora = BankAccount(1000, 1000)
Sara = BankAccount(1000, 3000)

print('User:Sara')
print(Sara.deposit(400).deposit(20).deposit(
    10).withdraw(700).yield_interest().balance)


print('User:nora')
print(nora.deposit(400).deposit(20).withdraw(400).withdraw(
    80).withdraw(200).withdraw(40).yield_interest().balance)
print(nora.display_account_info())
