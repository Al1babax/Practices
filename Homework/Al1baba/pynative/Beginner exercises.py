# 1
import decimal


def sum_or_multiply(num1, num2):

    if num1 * num2 > 1000:
        return num1 * num2
    else:
        return num1 + num2


# 2

def print_numbers():
    print("Printing current and previous number sum in a range(10)")
    sum1 = 0

    for number in range(10):
        sum1 = abs(number + (number - 1))
        if number <= 0:
            print(f"Current number {number} Previous number {abs(number)} Sum: {sum1 - 1}")
        elif number == 1:
            print(f"Current number {number} Previous number {abs(number - 1)} Sum: {sum1}")
        else:
            print(f"Current number {number} Previous number {abs(number - 1)} Sum: {sum1}")


# 3

def print_word():
    word = "pynative"

    print(word[::2])




# 4


def remove_chars(word, removed_letters):
    print(word[removed_letters:])

# 5

def same_number(list1):

    if list1[0] == list1[len(list1) - 1]:
        print("True")
        return True
    else:
        print("False")
        return False


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

#same_number(numbers_x)
#same_number(numbers_y)








# 6

def divisible_by_5(list1=[]):

    for number in range(len(list1)):
        if list1[number] % 5 == 0:
            print(list1[number])


#divisible_by_5([10, 20, 33, 46, 55])


# 7

def emma_count(sentence):
    count = 0
    emma_list = sentence.split(" ")

    for word in emma_list:
        if word == "Emma":
            count += 1

    print(f"Emma appeared {count} times")


# emma_count("Emma is good developer. Emma is a writer")


# 8

def stupid_flag():

    for row in range(5):
        for num in range((row + 1)):
            print((row + 1), end=" ")
        print()


# stupid_flag()


# 9

def palindrome_number(num1=121):

    if str(num1) == str(num1)[::-1]:
        print("Yes. given number is palindrome number")
    else:
        print("No, given number is not palindrome number")


# palindrome_number()


# 10

def weird_list():
    list1 = [10, 20, 25, 30, 35]
    list2 = [40, 45, 60, 75, 90]

    list3 = []

    for number in list1:
        if number % 2 != 0:
            list3.append(number)

    for number in list2:
        if number % 2 == 0:
            list3.append(number)

    print(list3)

# weird_list()


# 11

def reverse_integer(number):
    num = str(number)
    # print(num[::-1])
    x = 0
    number_length = len(num)
    while not x == number_length:
        print(f"{num[-x - 1]}", end=" ")
        x += 1


# reverse_integer(12345)


# 12

def income_tax(money=45_000):
    tax_dollars = 0

    if money > 20_000:
        tax_dollars += (money - 20_000) * 0.2
        money = money - (money - 20_000)  # should always be 20_000

    if money > 10_000:
        tax_dollars += (money - 10_000) * 0.1
        money = money - (money - 10_000)  # should always be 10_000

    # rest 10k not taxable

    print(tax_dollars)


income_tax()


# 13

# 1  2 3 4 5 6 7 8 9 10
# 2  4 6 8 10 12 14 16 18 20
# 3  6 9 12 15 18 21 24 27 30
# 4  8 12 16 20 24 28 32 36 40
# 5  10 15 20 25 30 35 40 45 50
# 6  12 18 24 30 36 42 48 54 60
# 7  14 21 28 35 42 49 56 63 70
# 8  16 24 32 40 48 56 64 72 80
# 9  18 27 36 45 54 63 72 81 90
# 10 20 30 40 50 60 70 80 90 100


def mutliplication_table():
    table_not_done = True
    numbers_done = 0

    while table_not_done:

        for num in range(10):
            print(f"{(numbers_done + 1) * (num + 1)}", end=" ")

        numbers_done += 1

        print()

        if numbers_done == 10:
            table_not_done = False

# mutliplication_table()


# 14

def half_pyramid():
    for row in range(5):
        for line in range(5 - row):
            print(f"*", end=" ")

        print()




# half_pyramid()


# 15

def exponent(base, exp):

    # print(pow(base, exp))
    # print(base ** exp)

    result = 1
    for x in range(exp):
        result = result * base

    print(result)

#exponent(2, -5)



