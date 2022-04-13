class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 1000


    def display_balance(self, name):
        print(name.name, "has $", name.account_balance)

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
        
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def make_transfer_from(self, amount):
        self.account_balance -= amount
        
    def make_transfer_to(self, amount):
        self.account_balance += amount
        
# users
dillan = User("Dillan")
tristan = User("Tristan")
zayn = User("Zayn")


#commands
dillan.make_deposit(50).make_deposit(100).make_deposit(200).make_withdrawal(900).display_balance(dillan)
tristan.make_deposit(50).make_deposit(100).make_withdrawal(200).make_withdrawal(900).display_balance(tristan)
zayn.make_deposit(50).make_withdrawal(100).make_withdrawal(200).make_withdrawal(900).display_balance(zayn)