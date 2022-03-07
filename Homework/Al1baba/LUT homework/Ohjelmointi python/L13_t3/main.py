import lib


def main():
    # file_name = "a.txt"
    file_data = None
    while True:
        lib.draw_menu()
        decision = int(input("Valintasi: "))

        if decision == 1:
            file_name = input("Anna luettavan tiedoston nimi: ")
            file_data = lib.read_file(file_name)
            # print(file_data)
            file_data = lib.time_to_datetime(file_data)
            # print(file_data)

        elif decision == 2:
            print(";Palautuksia viikonpäivittäin")
            # print(len(file_data))     # Checking that I have all the lines from the file --> 479 lines
            daily_data = lib.analyze_file(file_data)
            lib.print_data(daily_data)

        elif decision == 3:
            print(";Palautuksia tunneittain")
            hourly_data = lib.hourly_report(file_data)
            lib.print_data(hourly_data)

        elif decision == 4:
            start_time = input("Anna palautusjakson alkuaika [dd.mm.yyyy hh:mm]: ")
            # start_time = "21.9.2018 06:00"
            print(";Palautuksia ajanjaksolla")
            daily_week_data = lib.daily_reports_one_week(file_data, start_time)
            lib.print_data(daily_week_data)

        elif decision == 0:
            break
        else:
            print("Virheellinen valinta.")


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
