######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Sami Viik
# Opiskelijanumero: ########
# Päivämäärä: 09.11.2021
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: NaN
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################

def print_data(daily_hours, average_day_length):
    total_hours = sum(daily_hours)
    daily_hours = map(lambda x: str(x), daily_hours)    # Changing all the elements in a list from float to str
    hours_string = "h, ".join(daily_hours)      # Combining the hours list to a string
    hours_string = hours_string + "h, "		# Have to add the last h, which join function won't do
    print(f"Syötit seuraavat tunnit: {hours_string}yhteensä {total_hours} tuntia.")
    print(f"Keskimääräisen työpäivän pituus oli {average_day_length}h.")


def work_hours(daily_hours):
    amount_of_days = int(input("Kuinka monen päivän tiedot haluat syöttää: "))

    for x in range(amount_of_days):     # Adding all the hours to the daily_hours list
        daily_hours.append(float(input(f"Anna {x + 1}. päivän työtunnit: ")))

    average_day_length = sum(daily_hours) / amount_of_days      # Average length of the day
    print_data(daily_hours, average_day_length)     # Calling the print function


def main():
    daily_hours = []
    work_hours(daily_hours)


if __name__ == '__main__':
    print("Tämä ohjelma laskee töihin käytetyn ajan.")
    main()
