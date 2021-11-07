"""
Could save all the data written in this program to some data structure, and write all the data at once.
But I know that the file opened with write_palindrome function is not that big, so I can afford to open and close it
multiple times. If I encounter problem I write additional code to write_palindrome function if it is called too many
times to give out warning and not writing/opening the file anymore.
"""


def write_palindrome(str1):
    with open("L06T22.txt", "a") as f_w:
        f_w.write(f"{str1}\n")


def find_palindrome(file_name):     # Reading file, looking for words and calling another function to write them
    with open(file_name) as f_r:

        for line in f_r.readlines():    # Going through each line, removing the \n from them
            line = line[:-1]
            if not line.isdigit():      # Checking line is not a digit
                if line == line[::-1]:
                    print(f"Rivi '{line}' on palindromi.")
                    write_palindrome(line)
                else:
                    print(f"Rivi '{line}' ei ole palindromi.")
            else:
                print(f"Rivi '{line}' on numerorivi.")


def main():
    find_palindrome("L06T21.txt")


main()




