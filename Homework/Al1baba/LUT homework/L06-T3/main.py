written_lines = 0


def read_check_line(file_input="L06T31.txt", file_output="L06T32.txt"):    # Remove digit lines, count lines on the file
    global written_lines
    line_count = 0

    with open(file_input) as f_r:

        for line in f_r.readlines():
            if not line == "\n":    # If line is not empty
                line_count += 1     # Line count for every non-empty lines
                line = line[:-1]
                if not any(char.isdigit() for char in line):  # Using generator and any to check for digits(True)
                    write_line(line.lower(), file_output)    # Call write function with string with lower characters

    print(f"Luettiin {line_count} riviä tiedostosta '{file_input}'.")
    print(f"Kirjoitettiin {written_lines} riviä tiedostoon '{file_output}'.")


def write_line(str1, file_output):    # Write new lines, count lines on the file
    global written_lines

    with open(file_output, "a") as f_w:
        f_w.write(f"{str1}\n")

    written_lines += 1


def main():
    read_file = input("Anna luettavan tiedoston nimi: ")
    write_file = input("Anna kirjoitettavan tiedoston nimi: ")
    read_check_line(read_file, write_file)
    # read_check_line()
    print("Kiitos ohjelman käytöstä.")


if __name__ == "__main__":
    main()
