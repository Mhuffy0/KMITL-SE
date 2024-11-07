class SavingAccount:
    def __init__(self, bank_name, acc_name, acc_id, balance=0):
        self.bank_name = bank_name
        self.acc_name = acc_name
        self.acc_id = acc_id
        self.balance = balance
        self.transaction_history = []

    def deposit(self, money, person, date):
        self.balance += money
        self.transaction_history.append(f"{date}: {person} deposited {money}")

    def withdraw(self, money, person, date):
        if self.balance >= money:
            self.balance -= money
            self.transaction_history.append(f"{date}: {person} withdrew {money}")
        else:
            print("Insufficient funds for withdrawal.")

    def get_balance(self):
        return self.balance

    def print_statement(self):
        print(f"Bank: {self.bank_name}, Account Holder: {self.acc_name}, Balance: {self.balance}")
        for transaction in self.transaction_history:
            print(transaction)


class OverDrawnAccount(SavingAccount):
    def __init__(self, bank_name, acc_name, acc_id, balance=0, overdraft_limit=0):
        super().__init__(bank_name, acc_name, acc_id, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, money, person, date):
        if self.balance - money >= -self.overdraft_limit:
            self.balance -= money
            self.transaction_history.append(f"{date}: {person} withdrew {money}")
        else:
            print("Withdrawal exceeds overdraft limit.")
