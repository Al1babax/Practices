def check_leap_year(year) -> bool:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def main():
    year = int(input("Insert year: "))
    result = check_leap_year(year)
    if result is True:
        print("Is leap year!")
    else:
        print("Is not leap year!")


if __name__ == '__main__':
    main()
