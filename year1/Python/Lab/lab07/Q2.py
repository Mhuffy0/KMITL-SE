class BankAccount :
    def __init__(self, bank_name, owner_name, acc_num, balance):
        self.bank_name = bank_name
        self.owner_name = owner_name
        self.acc_num = acc_num
        self.balance = balance
        
    def deposit(self, money) :
        if money > 0: 
            self.balance = money + self.balance
        else: 
            print("deposit more than 0")
            self.balance
        print(f"{self.balance}")

    def withdraw(self, money) :
        if 0 < money < self.balance:
            self.balance = self.balance - money
        else:
            print("err")
        print(f"{self.balance}")
        
bank = BankAccount('SCD', 'Somchai', 12343, 50 )
bank.deposit(50)
bank.withdraw(25)