MENU = {
    "Ice cream": 5,
    "Pasta": 10,
    "Coca cola": 2,
    "Milkshake": 3,
    "Coffee": 1
}


def restaurant():
    total_price = 0
    still_run = True
    print(MENU)
    while still_run:
        order = input("What would you like to order? ")
        if order in MENU:
            total_price += MENU[order]
            print(f"{order} costs {MENU[order]}, total is {total_price}")
        elif order not in MENU:
            print(f"Sorry, we are fresh out of {order} today.")
        new_order = input(f"Would you like to order anything else y/n ")
        if new_order == "n":
            still_run = False

    print(f"Your total bill is {total_price}")


# restaurant()

"""
Credential database and username/password system
"""

CREDENTIALS = {
    "Mike": "secret123",
    "John": "balls000",
    "Karen": "paris08"
}


def login():
    username = input("Input your username: ")
    if username in CREDENTIALS:
        password = input("Input your password: ")
        if password == CREDENTIALS[username]:
            print("Login successful")
        else:
            print("Your password was wrong.")
    else:
        print("There is no such user in our database.")


# login()


#TODO rest of the exercise



