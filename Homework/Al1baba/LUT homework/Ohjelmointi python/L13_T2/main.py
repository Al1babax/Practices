import datetime as dt
import sys


def read_file(file_name):   # Reads the file
    file_data = []
    try:
        with open(file_name) as f:
            for x, line in enumerate(f.readlines()):
                line = line[:-1]    # Remove \n from the end of each line
                file_data.append(line.split(";"))
        file_data.pop(0)    # Removing first irrelevant line
        print("Tiedosto luettu.")
        return file_data
    except FileNotFoundError:
        print(f"Tiedoston '{file_name}' avaaminen epäonnistui.")
        sys.exit()


def time_to_datetime(data):  # Changing every element to datetime object if it is not empty

    for x, line in enumerate(data):
        temp_line = []
        for i, date in enumerate(line):
            if date != "":
                temp_line.append(dt.datetime.strptime(date, "%A, %d %B %Y, %I:%M %p"))
            else:
                temp_line.append("")
        data[x] = temp_line

    return data


def analyze_file(file):     # Using the datetime object to string to count how many entries per day
    weekday_count = {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0,
        "Yhteensä": 0
    }
    for data in file:
        for date in data:
            if date != "":
                if dt.datetime.strftime(date, "%A") in weekday_count:   # "Monday" == "Monday"
                    weekday_count[dt.datetime.strftime(date, "%A")] += 1
                    weekday_count["Yhteensä"] += 1

    return weekday_count


def print_data(data):
    for k, v in data.items():
        print(f"{k};{v}")


def draw_menu():
    print("""Anna haluamasi toiminnon numero seuraavasta valikosta: 
1) Lue tiedosto
2) Analysoi tiedot viikonpäivittäin
0) Lopeta""")


def main():
    # file_name = "a.txt"
    file_data = None
    while True:
        draw_menu()
        decision = int(input("Valintasi: "))

        if decision == 1:
            file_name = input("Anna luettavan tiedoston nimi: ")
            file_data = read_file(file_name)
            # print(file_data)
            file_data = time_to_datetime(file_data)
            # print(file_data)

        elif decision == 2:
            print(";Palautuksia viikonpäivittäin")
            # print(len(file_data))     # Checking that I have all the lines from the file --> 479 lines
            data = analyze_file(file_data)
            print_data(data)

        elif decision == 0:
            break
        else:
            print("Virheellinen valinta.")


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
