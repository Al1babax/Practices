sademäärä = {}


def main():
    for x in range(7):
        date = f"{x + 1}.1.2022"
        rain_amount = int(input(f"Anna sademäärä(mm) päivälle {date}: "))
        sademäärä[date] = rain_amount
    print(f"Viikon aikana satoi {sum(sademäärä.values())}mm vettä.")


if __name__ == '__main__':
    main()
