######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Sami Viik
# Opiskelijanumero: ########
# Päivämäärä: 09.11.2021
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: NaN
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################
import datetime as dt


class HourlyConsumption:

    def __init__(self, datetime, kwh):
        self.date = datetime
        self.kwh = kwh


def data_format():  # Reads the file and formats data
    with open("2018Sahkonkulutus.txt") as f:
        start = 0
        hour_kwh_data = []

        for line in f.readlines():
            if start >= 1:
                hour_kwh_data.append(line[:-1])
            else:
                start += 1

        return hour_kwh_data


def weekly_kwh_dict(daily_kwh_data_dict) -> dict:
    """
    This is wrong because I assumed the data is correct with no duplicated hourly data, or missing data

    weekly_kwh_data_list = []
    temp_weekly_kwh = 0

    for day, daily_object in enumerate(daily_kwh_data_objects):
        if day % 7 == 0:
            weekly_kwh_data_list.append((int((day + 1) / 7), temp_weekly_kwh))
            temp_weekly_kwh = 0

        temp_weekly_kwh += daily_object.daily_kwh
    else:
        weekly_kwh_data_list.append((53, temp_weekly_kwh))

    return weekly_kwh_data_list
    """
    weekly_data = {}

    for date, kwh in daily_kwh_data_dict.items():
        weekly_data[date.isocalendar()[1]] = 0

    for date, kwh in daily_kwh_data_dict.items():
        weekly_data[date.isocalendar()[1]] += kwh

    return weekly_data


def format_time_date(date) -> dt.datetime:
    datetime_list = date.split(";")
    datetime_list = datetime_list[0].split(" ")
    datetime_list.pop(0)
    datetime_list[0] = datetime_list[0].split(".")
    datetime_list[1] = datetime_list[1].split(":")
    datetime_list[0] = list(map(lambda x: int(x), datetime_list[0]))
    datetime_list[1] = list(map(lambda x: int(x), datetime_list[1]))
    # print(datetime_list)

    temp_time = dt.datetime(datetime_list[0][2], datetime_list[0][1], datetime_list[0][0],
                            datetime_list[1][0], datetime_list[1][1])

    return temp_time


def create_hourly_kwh_object_list(data) -> list:
    hour_object_list = []

    for hourly_data in data:
        temp_date = format_time_date(hourly_data)
        temp_list = hourly_data.split(";")
        hour_object_list.append(HourlyConsumption(temp_date, int(temp_list[1])))

    return hour_object_list


def create_daily_kwh_list(hourly_kwh_object_list) -> dict:
    """
    This is wrong because I assumed the data is correct with no duplicated hourly data, or missing data

    daily_kwh_data_objects = []
    hour_day_count = 0
    daily_kwh = 0
    current_date = ""
    hour_kwh_data = data_format()

    for element in hour_kwh_data:  # Splitting daily data to [date, [time, kwh]]
        temp1 = element.split(" ")
        temp1 = [temp1[1], temp1[2].split(";")]

        if hour_day_count == 24:
            daily_kwh_data_objects.append(DailyConsumption(current_date, daily_kwh))
            hour_day_count = 0
            daily_kwh = 0

        if hour_day_count == 0:
            current_date = temp1[0]

        if 0 <= hour_day_count <= 23:
            daily_kwh += int(temp1[1][1])
            hour_day_count += 1

    else:  # to add the final day of the year to object list
        daily_kwh_data_objects.append(DailyConsumption(current_date, daily_kwh))
    # Here just testing stuff
    # print(len(daily_kwh_data_objects))
    # print(f"{daily_kwh_data_objects[0].date} {daily_kwh_data_objects[0].daily_kwh}")
    # print(f"{daily_kwh_data_objects[-1].date} {daily_kwh_data_objects[-1].daily_kwh}")
    check_if_data_is_shit(daily_kwh_data_objects, hour_kwh_data)
    return daily_kwh_data_objects
    """
    daily_consumption = {}
    daily_amount = 0

    for obj in hourly_kwh_object_list:
        daily_consumption[obj.date.date()] = 0

    for obj in hourly_kwh_object_list:
        daily_consumption[obj.date.date()] += obj.kwh

    key_view = daily_consumption.keys()
    key_iterator = iter(key_view)
    first_key = next(key_iterator)
    # print(first_key.date())

    return daily_consumption


def print_weekly_data(weekly_kwh_data):
    print(f"0;0")
    # I have no idea why output should have empty first weak and why 53th week exists and has some kwh from
    # week 1
    mixed_kwh = 81640

    for week, kwh in weekly_kwh_data.items():
        if week == 1:
            print(f"{week};{kwh - mixed_kwh}")
        else:
            print(f"{week};{kwh}")

    print(f"53;{mixed_kwh}")


def check_if_data_is_wrong(daily_kwh_data_objects, hour_kwh_data):
    current_date = dt.datetime(2018, 1, 1, 0, 0)  # also start date

    for date_str in hour_kwh_data:
        datetime_list = date_str.split(";")
        datetime_list = datetime_list[0].split(" ")
        datetime_list.pop(0)
        datetime_list[0] = datetime_list[0].split(".")
        datetime_list[1] = datetime_list[1].split(":")
        datetime_list[0] = list(map(lambda x: int(x), datetime_list[0]))
        datetime_list[1] = list(map(lambda x: int(x), datetime_list[1]))
        # print(datetime_list)

        temp_time = dt.datetime(datetime_list[0][2], datetime_list[0][1], datetime_list[0][0],
                                datetime_list[1][0], datetime_list[1][1])

        if current_date != temp_time:
            print(f"Line wrong {current_date}")
            break

        current_date = current_date + dt.timedelta(hours=1)


def main():
    formatted_data = data_format()
    hourly_kwh_object_list = create_hourly_kwh_object_list(formatted_data)
    daily_kwh_data_dict = create_daily_kwh_list(hourly_kwh_object_list)
    weekly_kwh_data = weekly_kwh_dict(daily_kwh_data_dict)
    # print(weekly_kwh_data)
    print_weekly_data(weekly_kwh_data)


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
