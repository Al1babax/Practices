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
3) Analysoi tiedot tunneittain
4) Analysoi tiedot 24 tunnin jaksoissa
0) Lopeta""")


def hourly_report(file):
    hourly_dict = {}
    total_counter = 0

    for data in file:
        for date in data:
            if date != "":
                # hour = dt.datetime.strftime(date, "%H")
                hour = str(date.hour)
                # print(date.hour)
                if hour not in hourly_dict:
                    hourly_dict[hour] = 0
                if hour in hourly_dict:
                    hourly_dict[hour] += 1
                    total_counter += 1

    hourly_dict = dict(sorted(hourly_dict.items(), key=lambda x: int(x[0])))    # No idea why pycharm gives warning here
    # print(hourly_dict)
    hourly_dict["Yhteensä"] = total_counter

    return hourly_dict


def daily_reports_one_week(file, start_time):
    start_time = dt.datetime.strptime(start_time, "%d.%m.%Y %H:%M")
    timedelta = 1
    next_day = start_time + dt.timedelta(days=timedelta)
    daily_dict = {k: 0 for k, v in enumerate(range(7))}
    total_counter = 0
    day = 0

    for day in range(len(daily_dict)):  # Going over each day for one week
        for data in file:   # Checking one day
            for date in data:
                if date != "" and start_time <= date <= next_day:
                    daily_dict[timedelta - 1 + day] += 1
                    total_counter += 1
        start_time = start_time + dt.timedelta(days=timedelta)
        next_day = start_time + dt.timedelta(days=timedelta)
        day += 1

    daily_dict["Yhteensä"] = total_counter
    return daily_dict


if __name__ == '__main__':
    pass
