import datetime as dt


def draw_calendar(year=2005, month=9):
    print("Kalenteri näyttää seuraavalle:")
    date1 = dt.datetime(year, month, 1)
    start_day = date1.strftime("%u")
    days_in_month = 0

    temp_date = date1
    while int(temp_date.month) == month:    # To get total days in a month
        days_in_month = int(temp_date.day)
        temp_date += dt.timedelta(days=1)

    # print(days_in_month)
    print("Ma Ti Ke To Pe La Su")
    for _ in range(int(start_day) - 1):     # To print empty lines before first day of the month starts
        print("  ", end=" ")

    for x in range(days_in_month):  # To print every day for the month
        if start_day == "7":
            print("{:>2}".format(x + 1), end=" ")
            print("")
        else:
            print("{:>2}".format(x + 1), end=" ")
        date1 += dt.timedelta(days=1)
        start_day = date1.strftime("%u")


def main():
    year = int(input("Anna vuosi: "))
    month = int(input("Anna kuukausi: "))
    draw_calendar(year, month)
    # draw_calendar()


if __name__ == '__main__':
    main()
