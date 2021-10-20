"""
Program to convert any decimal number to hexadecimal number
"""


import math

hexa_dict = {}

for number in range(10):
    hexa_dict[number] = number

value_list = ["A", "B", "C", "D", "E", "F"]

for number in range(6):
    hexa_dict[number+10] = value_list[number]


def dec_to_hex(dec=479):
    hex_value = ""
    remainder_list = []
    value = dec
    x = 0

    while value != 0:

        remainder_list.append(math.floor(value % 16))
        if remainder_list[x] > 9:
            remainder_list[x] = value_list[remainder_list[x] - 10]
        x += 1
        value = math.floor(value) / 16

    for value in range(len(remainder_list)):
        remainder_list[value] = str(remainder_list[value])

    remainder_list.reverse()
    remainder_list.pop(0)

    # print(remainder_list)

    for x in range(len(remainder_list)):
        hex_value += remainder_list[x]

    print(f"0x{hex_value}")




dec_to_hex(3945893745)


