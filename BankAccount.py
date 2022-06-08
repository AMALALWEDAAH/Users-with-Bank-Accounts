
class BankAccount:
    # don't forget to add some default values for these parameters!# your code here! (remember, this is where we specify the attributes for our class)
    def __init__(self, int_rate=0.02, balance=0.0):
        self.int_rate = int_rate
        self.balance = balance
        self.interset = 0

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
            f"Account Balance:${self.balance}\nyield interset:{self.interset}\n")
        return self

    def yield_interest(self):
        # your code herecopy
        if self.balance > 0:
            self.interset = self.balance*self.int_rate
            return self


# nora = BankAccount(0.02, 1000)
# Sara = BankAccount(0.02, 3000)

# print('User:Sara')

# Sara.deposit(10).deposit(20).deposit(30).withdraw(
#     70).yield_interest().display_account_info()


# print('User:nora')
# nora.deposit(400).deposit(20).withdraw(20).withdraw(80).withdraw(
#     200).withdraw(40).yield_interest().display_account_info()
