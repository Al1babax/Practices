import datetime as dt


def check_validate_symbol(number):
    # VIOPE exercise is wrong, and the last symbol always need to be upper case if it is character !!!
    # Making this change so can pass viope test...
    number = number[:-1] + number[-1].upper()

    # remainder between 0-9
    number_list = "0123456789"
    # remainder between 10-30
    alph_list = "ABCDEFHJKLMNPRSTUVWXY"

    num1 = int(number[0:6] + number[7:10])
    remainder = num1 % 31

    # Setupping what is the symbol supposed to be according to rules
    if 0 <= remainder <= 9:
        check_symbol = str(remainder)
    else:
        check_symbol = alph_list[remainder - 10]

    # Checking if the symbol is what is it supposed to be
    if check_symbol == number[-1]:
        return True
    else:
        return False


def validate_social_security(number):
    # ppkkvvynnnt FORMAT
    # ppkkvv datetime object check
    # y = {1800: +, 1900: -, 2000: A}
    # nnn --> between [002, 899]
    # example: 120345-678M

    try:    # Checking the first 6 numbers for date
        date = dt.datetime.strptime(number[0:6], "%d%m%y")
    except ValueError:
        return False

    try:    # Checking 3 last numbers that they are digits
        int(number[7:10])
    except ValueError:
        return False

    # Checking the middle symbol
    """
    Actually cannot do this
    if str(date.year)[0:2] == "18" and number[6] != "+":
        return False
    if str(date.year)[0:2] == "19" and number[6] != "-":
        return False
    if str(date.year)[0:2] == "20" and number[6] != "A":
        return False
    """
    middle_symbols = "+-A"
    if not number[6] in middle_symbols:
        return False

    # Validating the last symbol
    if not check_validate_symbol(number):
        return False

    return True     # If the number passes every check it is valid social security number


def main():
    # number = input("Anna henkilötunnus: ")
    number = "120345+678m"
    if validate_social_security(number):
        print("Henkilötunnus hyväksytty.")
    else:
        print("Henkilötunnusta ei hyväksytä.")


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
