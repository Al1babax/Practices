def read_file(file):
    err_log = {}
    err_log2 = {}  # ... gotta make two logs so can prio errors for right output
    file_dict = {
        "ID": {
            "Comment": "",
            "Points": "",
            "Original_line_number": 0,
            "Original_line": ""
        }
    }
    file_dict.pop("ID")
    try:
        with open(file) as f:
            for x, line in enumerate(f.readlines()):
                try:
                    temp_line = line.split(";")
                    if len(temp_line[0]) != 4 or not temp_line[0].isdigit() and len(temp_line) == 3:
                        err_log2[x + 1] = f"Virheellinen ID, rivillä {x + 1}: {(';'.join(temp_line))[:-1]}"
                    if len(temp_line) == 3 and temp_line[0] not in file_dict:
                        file_dict[temp_line[0]] = {
                            "Comment": temp_line[1],
                            "Points": temp_line[2][:-1],
                            "Original_line_number": x + 1,
                            "Original_line": line[:-1]
                        }
                    else:
                        err_log[x + 1] = f"Väärä määrä arvoja, rivillä {x + 1}: {(';'.join(temp_line))[:-1]}"
                except ValueError as e:
                    # print(f"Väärä määrä arvoja, rivillä {x}: {';'.join(temp_line)}")
                    # error_log.append(f"Väärä määrä arvoja, rivillä {x}: {';'.join(temp_line)}")
                    err_log[x + 1] = f"Virheellinen ID, rivillä {x + 1}: {(';'.join(temp_line))[:-1]}"
    except FileNotFoundError:
        print(f"Tiedoston '{file}' avaaminen epäonnistui.")
    err_log = {**err_log, **err_log2}
    return file_dict, err_log


def check_comment(comment):
    new_comment = ""
    accepted_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    for symbol in comment:
        if symbol.upper() in accepted_alphabet or symbol.isdigit():
            new_comment += symbol
    return new_comment


def clean_file(file):
    err_log = {}
    new_file = {
        "ID": {
            "Comment": "",
            "Points": "",
            "Original_line_number": 0,
            "Original_line": ""
        }
    }
    new_file.pop("ID")
    for num, ID in enumerate(file.items()):
        # print(ID[1].get("Comment"))
        try:
            # print(ID)
            if len(ID[0]) == 4 and ID[0].isdigit():
                new_id = ID[0]
                new_comment = check_comment(ID[1].get("Comment"))
                new_points = int(ID[1].get("Points"))
                if new_points == 0:
                    new_points += 1
                new_file[new_id] = {"Comment": new_comment, "Points": new_points}
            else:
                # print(f"Virheellinen ID, rivillä {num - 1}:")
                # error_log.append(f"Virheellinen ID, rivillä {num - 1}:")
                err_log[ID[1].get(
                    "Original_line_number")] = f"Virheellinen ID, rivillä {ID[1].get('Original_line_number')}: {ID[1].get('Original_line')}"
        except ValueError:
            # print("Pointsit ei ollu ok")
            pass
    return new_file, err_log


def main():
    error_log = []
    file1 = "L12T3_1.txt"
    file2 = "L12T3_2.txt"

    formatted_file1, er1_log = read_file(file1)
    error_log.append(er1_log)
    # formatted_file2 = read_file(file2)

    clean_file1, er2_log = clean_file(formatted_file1)
    error_log.append(er2_log)
    # clean_file2 = clean_file(formatted_file2)

    print(error_log[0])
    print(error_log[1])
    final_error = {**error_log[1], **error_log[0]}
    final_error.pop(1)
    print(dict(sorted(final_error.items())))


if __name__ == '__main__':
    main()
