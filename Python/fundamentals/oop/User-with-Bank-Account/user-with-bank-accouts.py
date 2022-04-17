class BankAccount:

    def __init__(self, name, int_rate = .05, balance = 0):
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


class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 1000 
        self.account = BankAccount(name)
        self.account_type = BankAccount("Savings")
    
    def make_deposit1(self, amount):
        self.account_balance += amount

    def make_transfer_from(self, amount):
        self.account_balance -= amount
        
    def make_transfer_to(self, amount):
        self.account_balance += amount
        
# users
dillan = User("Dillan")
tristan = User("Tristan")
zayn = User("Zayn")


#commands DILLAN
print(str(dillan.name) + "'s " + str(dillan.account_type.name))
print("Current Balance:")
# print("$", dillan.account_balance)
print("$"+str(dillan.account.balance))
# x = dillan.account_balance
x1 = dillan.account.balance
print("--->Deposited:")
dillan.account.make_deposit(50)
print("$" + str(dillan.account.balance - x1))
# print("$", dillan.account_balance - x)
print("Current Balance:")
# print("$", dillan.account_balance)
print("$"+str(dillan.account.balance))
# x = dillan.account_balance
x1 = dillan.account.balance

print("--->Deposited:")
dillan.account.make_deposit(69)
print("$" + str(dillan.account.balance - x1))
print("Current Balance:")
print("$"+str(dillan.account.balance))
x1 = dillan.account.balance

print("--->Deposited:")
dillan.account.make_deposit(99)
print("$" + str(dillan.account.balance - x1))
print("Current Balance:")
print("$"+str(dillan.account.balance))
x1 = dillan.account.balance

print("--->Withdrew:")
dillan.account.make_withdrawal(156)
print("$" + str(dillan.account.balance - x1))
print("Current Balance:")
print("$"+str(dillan.account.balance))
x1 = dillan.account.balance

print()

#commands TRISTAN
print(str(tristan.name) + "'s " + str(tristan.account_type.name))
print("Current Balance:")
print("$"+str(tristan.account.balance))
x1 = tristan.account.balance
print("--->Deposited:")
tristan.account.make_deposit(50)
print("$" + str(tristan.account.balance - x1))
print("Current Balance:")
print("$"+str(tristan.account.balance))
x1 = tristan.account.balance

print("--->Deposited:")
tristan.account.make_deposit(89)
print("$" + str(tristan.account.balance - x1))
print("Current Balance:")
print("$"+str(tristan.account.balance))
x1 = tristan.account.balance

print("--->Deposited:")
tristan.account.make_deposit(564)
print("$" + str(tristan.account.balance - x1))
print("Current Balance:")
print("$"+str(tristan.account.balance))
x1 = tristan.account.balance

print("--->Withdrew:")
tristan.account.make_withdrawal(232)
print("$" + str(tristan.account.balance - x1))
print("Current Balance:")
print("$"+str(tristan.account.balance))
x1 = tristan.account.balance

print("--->Withdrew:")
tristan.account.make_withdrawal(134)
print("$" + str(tristan.account.balance - x1))
print("Current Balance:")
print("$"+str(tristan.account.balance))
x1 = tristan.account.balance

print()

#commands ZAYN    
print(str(zayn.name) + "'s " + str(zayn.account_type.name))
print("Current Balance:")
print("$"+str(zayn.account.balance))
x1 = zayn.account.balance
print("--->Deposited:")
zayn.account.make_deposit(50)
print("$" + str(zayn.account.balance - x1))
print("Current Balance:")
print("$"+str(zayn.account.balance))
x1 = zayn.account.balance

print("--->Deposited:")
tristan.account.make_deposit(89)
print("$" + str(tristan.account.balance - x1))
print("Current Balance:")
print("$"+str(tristan.account.balance))
x1 = tristan.account.balance

print("--->Deposited:")
zayn.account.make_deposit(990)
print("$" + str(zayn.account.balance - x1))
print("Current Balance:")
print("$"+str(zayn.account.balance))
x1 = zayn.account.balance

print("--->Withdrew:")
zayn.account.make_withdrawal(100)
print("$" + str(zayn.account.balance - x1))
print("Current Balance:")
print("$"+str(zayn.account.balance))
x1 = zayn.account.balance

print("--->Withdrew:")
zayn.account.make_withdrawal(300)
print("$" + str(zayn.account.balance - x1))
print("Current Balance:")
print("$"+str(zayn.account.balance))
x1 = zayn.account.balance

print()