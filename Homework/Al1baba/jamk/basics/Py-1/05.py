bank_balance = 2000
print(f"Bank account balance: {bank_balance}")
euros = int(input("How many euros will be added to the balance? "))
cents = int(input("How many cents will be added to the balance? "))
bank_balance += euros + (cents / 100)
print(f"Bank account balance: {bank_balance}")
