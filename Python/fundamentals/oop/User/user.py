class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 1000
    
    def make_deposit(self, amount):
        self.account_balance += amount
        
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def make_transfer_from(self, amount):
        self.account_balance -= amount
        
    def make_transfer_to(self, amount):
        self.account_balance += amount
        
# users
dillan = User("Dillan")
tristan = User("Tristan")
zayn = User("Zayn")


#commands
print(dillan.name)
print("Current Balance:")
print("$", dillan.account_balance)
x = dillan.account_balance

print("--->Deposited:")
dillan.make_deposit(50)
print("$", dillan.account_balance - x)
print("Current Balance:")
print("$", dillan.account_balance)
x = dillan.account_balance

print("--->Deposited:")
dillan.make_deposit(69)
print("$", dillan.account_balance - x)
print("Current Balance:")
print("$", dillan.account_balance)
x = dillan.account_balance

print("--->Deposited:")
dillan.make_deposit(99)
print("$", dillan.account_balance - x)
print("Current Balance:")
print("$", dillan.account_balance)
x = dillan.account_balance

print("--->Withdrawal:")
dillan.make_withdrawal(156)
print("$", dillan.account_balance - x)
print("Current Balance:")
print("$", dillan.account_balance)
x = dillan.account_balance

print("--->Transfered:")
y = 200
dillan.make_transfer_from(y)
print("$", dillan.account_balance - x)
print("Current Balance:")
print("$", dillan.account_balance)

print()

print(tristan.name)
print("Current Balance:")
print("$", tristan.account_balance)
x = tristan.account_balance

print("--->Deposited:")
tristan.make_deposit(400)
print("$", tristan.account_balance - x)
print("Current Balance:")
print("$", tristan.account_balance)
x = tristan.account_balance


print("--->Deposited:")
tristan.make_deposit(560)
print("$", tristan.account_balance - x)
print("Current Balance:")
print("$", tristan.account_balance)
x = tristan.account_balance

print("--->Withdrawal:")
tristan.make_withdrawal(35)
print("$", tristan.account_balance - x)
print("Current Balance:")
print("$", tristan.account_balance)

print("--->Withdrawal:")
tristan.make_withdrawal(236)
print("$", tristan.account_balance - x)
print("Current Balance:")
print("$", tristan.account_balance)

print()

print(zayn.name)
print("Current Balance:")
print("$", zayn.account_balance)
x = zayn.account_balance

print("--->Deposited:")
zayn.make_deposit(6400)
print("$", zayn.account_balance - x)
print("Current Balance:")
print("$", zayn.account_balance)
x = zayn.account_balance

print("--->Withdrawal:")
zayn.make_withdrawal(335)
print("$", zayn.account_balance - x)
print("Current Balance:")
print("$", zayn.account_balance)
x = zayn.account_balance

print("--->Withdrawal:")
zayn.make_withdrawal(435)
print("$", zayn.account_balance - x)
print("Current Balance:")
print("$", zayn.account_balance)
x = zayn.account_balance
print("--->Withdrawal:")
zayn.make_withdrawal(236)
print("$", zayn.account_balance - x)
print("Current Balance:")
print("$", zayn.account_balance)
x = zayn.account_balance

print("--->Received:")
zayn.make_transfer_to(y)
print("$", zayn.account_balance - x)
print("Current Balance:")
print("$", zayn.account_balance)