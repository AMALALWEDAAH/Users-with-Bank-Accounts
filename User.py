from BankAccount import BankAccount
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
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def transfer_money(self, user, amount):
        self.account_balance -= amount
        user.account_balance += amount
        return self


guido = User("Guido van Rossum", "guido@python.com", 150)
monty = User("monty", "monty@python.com", 55)
print(guido.name)
print(monty.name)
guido.make_withdrawal(15)

guido.display_user_balance()

# Create 3 instances of the User class
nora = User('nora', 'nora@python.com', 1000)
Sara = User('Sara', 'Sara@python.com', 3000)
lama = User('lama', 'lama@python.com', 4000)

print(Sara.account.deposit(400).deposit(20).deposit(
    10).withdraw(700).yield_interest().balance)

print('User:nora')
print(nora.account.deposit(400).deposit(20).withdraw(400).withdraw(
    80).withdraw(200).withdraw(40).yield_interest().balance)
print(nora.display_account_info())
# nora.make_deposit(100)
# print(nora.account_balance)
# nora.make_withdrawal(444)
# print(nora.account_balance)
# monty.display_user_balance()
# print(nora.display_user_balance())


# # Have the first user make 3 deposits and 1 withdrawal and then display their balance
# print('User:Sara')
# Sara.make_deposit(400)
# Sara.make_deposit(20)
# Sara.make_deposit(10)
# Sara.make_withdrawal(700)
# print(Sara.display_user_balance())


# # Have the second user make 2 deposits and 2 withdrawals and then display their balance
# print('User:Sara')
# lama.make_deposit(400)
# lama.make_deposit(20)
# lama.make_withdrawal(400)
# lama.make_withdrawal(80)
# print(lama.display_user_balance())

# # Have the third user make 1 deposits and 3 withdrawals and then display their balance
# print('User:lama')
# lama.make_deposit(400)
# lama.make_withdrawal(800)
# lama.make_withdrawal(200)
# lama.make_withdrawal(100)
# print(lama.display_user_balance())
# print('---')
# # transfer_money
# Sara.transfer_money(nora, 32)
# print(Sara.display_user_balance())
# print(nora.display_user_balance())
# ######
