def is_interesting(number, awesome_phrases):
    number_list = [number + 1 + x for x in range(2)]
    # print(number_list)
    if number >= 100:
        if check_zeros(number) or same_digit(number) or numbers_in_order(number) or number_is_palindrome(number):
            return 2
        elif number_is_awesome(number, awesome_phrases):
            return 2
    for number in number_list:
        if number >= 100:
            if check_zeros(number) or same_digit(number) or numbers_in_order(number) or number_is_palindrome(number):
                return 1
            elif number_is_awesome(number, awesome_phrases):
                return 1
    return 0


def check_zeros(number):
    # Case 1: All numbers after first digit are zeros
    number_str = str(number)
    numbers_except_first = int(number_str[1:])
    if numbers_except_first == 0:
        print("check zeros")
        return True


def same_digit(number):
    number_str = str(number)
    for x in range(len(number_str)):
        if number_str[0] != number_str[x]:
            return False
    print("same digit")
    return True


def numbers_in_order(number):
    number = str(number)
    number1 = number
    number2 = number[::-1]
    result1 = check_order(number1)
    result2 = check_order(number2)
    if result1 == 2 or result2 == 2:
        print("numbers in order")
        return True
    else:
        return False


def check_order(number: str):
    for x in range(len(number) - 1):
        number1 = number[x]
        number2 = number[x + 1]
        if int(number1) == 9 and int(number2) != 0:
            return 0
        elif int(number1) + 1 != int(number2) and int(number1) != 9:
            return 0
        elif x + 2 == len(number) and int(number1) + 1 == int(number2) and int(number1) != 0:
            return 2
        elif int(number1) == 9 and int(number2) == 0 and x + 2 == len(number):
            return 2


def number_is_palindrome(number):
    if str(number) == str(number)[::-1]:
        print("number is palindrome")
        return True


def number_is_awesome(number, array):
    for x in range(len(array)):
        if number == array[x]:
            print("number is awesome")
            return True
    return False

print(is_interesting(109, [1337, 256]))


