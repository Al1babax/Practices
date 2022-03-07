age = int(input("How old are you? "))

if age < 13:
    print("child")
elif 13 <= age <= 19:
    print("teen")
elif 20 <= age <= 65:
    print("adult")
else:
    print("senior")
