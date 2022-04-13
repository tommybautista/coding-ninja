class BankAccount:

    def __init__(self, name, int_rate = 0.05, balance = 0):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        
    def display_account_info_1(self):
        print("Current Balance: $", self.balance)
        return self
    
    def make_deposit(self, amount):
        self.balance += amount
        return self
        
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def yield_interest(self, int_rate):
        self.balance -= (self.balance * int_rate)
        return self
        
    def display_account_info_2(self):
        print("Ending Balance: $", self.balance)
        return self
        
account1 = BankAccount("Account1")
account2 = BankAccount("Account2")

#commands
print(account1.name)
account1.display_account_info_1().make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100).yield_interest(account1.int_rate).display_account_info_2()

print()

print(account2.name)
account2.display_account_info_1().make_deposit(200).make_deposit(200).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200).yield_interest(account2.int_rate).display_account_info_2()