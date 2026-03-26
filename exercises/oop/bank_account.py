class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print(f"Insufficient funds. Balance: ${self.balance}")

    def get_balance(self):
        return self.balance


bank = BankAccount()
bank.deposit(100)
bank.deposit(50)
bank.withdraw(30)
bank.withdraw(200)
print(f"Balance: ${bank.get_balance()}")
