from typing import List, Union, Any

"""
From /etc/passwd, create a dict in which the keys are the usernames (as in the
main exercise) and the values are themselves dicts with keys (and appropriate
values) for user ID, home directory, and shell.
"""


def dict_of_file():
    output_dict = {}

    with open("passwd.txt") as f, open("test.txt", "a") as t:

        for line in f:

            temp_list = line.split(":")  # Making temp list of the line on file
            temp_list: list[Union[str, Any]] = list(filter(None, temp_list))  # Removing empty elements

            if temp_list[-1].endswith("\n"):  # Removing all \n from lines in the end
                temp_list[-1] = temp_list[-1].strip("\n")

            if not temp_list[0].startswith(("#", "\n")):  # Creating the output dictionary
                output_dict[temp_list[0]] = {}  # There is probably better way to do this, but I have no idea
                output_dict[temp_list[0]]["ID"] = temp_list[2]
                output_dict[temp_list[0]]["Home Directory"] = temp_list[-2]
                output_dict[temp_list[0]]["Shell"] = temp_list[-1]
                print(output_dict)
                # t.write(str(output_dict))
                # t.write("\n")
                output_dict.clear()


# for _ in range(1_00000):  # Just messing around and creating a file repeating dict output :D
    # dict_of_file()
dict_of_file()

