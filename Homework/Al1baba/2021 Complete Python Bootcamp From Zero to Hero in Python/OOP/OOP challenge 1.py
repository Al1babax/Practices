class BankAccount():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted")
        print(f"Your account balance is now: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdraw successful")
            print(f"Your account balance is now: {self.balance}")
        else:
            print(f"You don't have enough balance on your account")
            print(f"Account balance: {self.balance}")

    def __str__(self):
        return f"Account owner:   {self.owner}\n" \
               f"Account balance: {self.balance}"


acct1 = BankAccount("Sam", 100)

acct1.deposit(200)
print(acct1)
acct1.withdraw(250)
acct1.withdraw(100)








