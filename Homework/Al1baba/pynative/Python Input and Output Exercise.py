# 2

#print('Name', 'Is', 'James', sep="**")


# 3
"""
Decimal to octal converter
"""
import math
from builtins import classmethod


def dec_to_octal(num1=7562):

    result = []

    while math.floor(num1) != 0:
        quo = num1 % 8
        result.append(str(quo))
        num1 = math.floor(num1 / 8)

    result.reverse()
    result = "".join(result)

    return int(result)


# print(dec_to_octal(454545))

# 4

num = 458.541315

# print(round(num, 2))

# print(f"{num:.2f}")

# print("%.2f" % num)


# 5

number_dict = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth"
}


def ask_numbers_for_list():
    number_list = []
    for number in range(5):
        number1 = input(f"Input {number_dict[number + 1]} number to your list: ")
        number_list.append(number1)
    else:
        result = f"Your final number list is:\n{number_list}"

    return result

# print(ask_numbers_for_list())


# 6
"""
Opens both files and calls function with those files as parameters, function reads first file, removes 4th line
and then copy everything left in f_lines variable
"""


def write_next_txt(file1, file2):

    f_lines = file1.readlines()
    f_lines.pop(4)
    file2.writelines(f_lines)


with open("testfile.txt", "r") as f1, open("new_testfile.txt", "w+") as f2:
    # write_next_txt(f1, f2)
    pass


# 7
# Time to learn how to make loops the pythonian way
def ask_names():
    name1, name2, name3 = [input(f"Input name: ") for _ in range(3)]
    return name1, name2, name3


# print(ask_names())

# 8

totalMoney = 1000
quantity = 3
price = 450

# print(f"I have {totalMoney} dollars so I can buy {quantity} football for {price} dollars.")

# 9
import os

fsize = os.path.getsize("new_testfile.txt")

if fsize == 0:
    print("The file is empty: " + str(fsize))
else:
    print("The file is not empty: " + str(fsize))

# 10

# Quite stupid this last one, not even gonna do :D:D




























