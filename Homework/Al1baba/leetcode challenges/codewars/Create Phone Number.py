def create_phone_number(n):
    n = map(lambda x: str(x), n)
    phone_number = "".join(n)
    return f"({phone_number[0:3]}) {phone_number[3:6]}-{phone_number[6:]}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))    # => returns "(123) 456-7890"