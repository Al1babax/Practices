"""
Taking data from passwd.txt file and outputting a dictionary with username as key and userID as value
On file index 0 is username and index 2 is the userID  ---> indexes are separated by :
"""
from collections import defaultdict


def passwd_to_dict():
    output_dict = {}

    with open("passwd.txt") as f:  # Iterating each line and taking username and userID and adding them to output_dict
        for line in f:
            temp_list = line.split(":")
            if not temp_list[0].startswith(("#", "\\n")):
                output_dict[temp_list[0]] = temp_list[2]

    return output_dict


# print(passwd_to_dict())


"""
Reading through the file and making a dict where keys are login shells (final field on each line) and values will be
list of users for whom that shell is defined as their login shell.
"""


def login_shell_dict():
    output_dict2 = defaultdict(list)    # Making output dict as a list, so I can append usernames to login shell

    with open("passwd.txt") as f1:

        for line in f1:
            temp_list = line.split(":")     # Making temp list of the line on file

            if temp_list[-1].endswith("\n"):    # Removing all \n from lines in the end
                temp_list[-1] = temp_list[-1].strip("\n")

            if not temp_list[0].startswith(("#", "\n")):    # Creating the output dictionary
                output_dict2[temp_list[-1]].append(temp_list[0])

    return output_dict2


# print(dict(login_shell_dict()))


def silly_dict():
    # numbers = input("Input numbers with spaces ")
    final_dict = defaultdict(list)
    numbers = "4 56 7  8 6 5  4 54    78 4  34  345"
    temp_list = numbers.split()

    for number in temp_list:
        for x in range(0, int(number) + 1):
            if int(number) % (x + 1) == 0:
                final_dict[x + 1].append(number)

    result = sorted(final_dict.items(), key=lambda y: y[0])     # Sorting the dictionary by keys
    print(dict(result))


# silly_dict()















