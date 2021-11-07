def check_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def check_virke(str1):
    word_list = str1.split(" ")
    if len(word_list) > 1 and word_list[-1][-1] == ".":     # Checking that sentence length > 1 and last char is dot
        return True
    else:
        return False


def write_read_plus(file):
    # Opening every file with context manager
    with open(file, "r") as f, open("kokonaisluku.txt", "w+") as k, open("desimaaliluku.txt", "w+") as d, open("sana.txt", "w+") as s, open("virke.txt", "w+") as v:
        for line in f.readlines():
            # print(line[:-1])
            if line[:-1].isdigit():
                # print("k: " + line[:-1])
                k.write(f"{line[:-1]}\n")
            elif check_float(line[:-1]):
                # print("d: " + line[:-1])
                d.write(f"{line[:-1]}\n")
            elif line[:-1].isalpha():
                # print("s: " + line[:-1])
                s.write(f"{line[:-1].upper()}\n")
            elif check_virke(line[:-1]):
                # print("v: " + line[:-1])
                v.write(f"{line[:-1].lower().capitalize()}\n")
            else:
                print(f"Tunnistamaton rivi '{line[:-1]}'.")


def main():
    write_read_plus("riveja.txt")
    pass


if __name__ == '__main__':
    main()

