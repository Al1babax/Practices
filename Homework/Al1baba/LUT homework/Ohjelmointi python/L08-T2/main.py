######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Sami Viik
# Opiskelijanumero: ########
# Päivämäärä: 09.11.2021
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: NaN
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################
import datetime
import datetime as dt
# apparently cannot use extra modules...
# from dateutil.relativedelta import relativedelta


def create_datetime_object():
    data = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")
    datetime_object = dt.datetime.strptime(data, "%d.%m.%Y %H:%M")
    print(f"Annoit vuoden {datetime_object.year}")
    print(f"Annoit kuukauden {datetime_object.month}")
    print(f"Annoit päivän {datetime_object.day}")
    print(f"Annoit tunnin {datetime_object.hour}")
    print(f"Annoit minuutin {datetime_object.minute}")
    return datetime_object


def how_old_in_2000():
    data = input("Anna syntymäpäiväsi muodossa pp.kk.vvvv: ")
    date_object = (dt.datetime.strptime(data, "%d.%m.%Y")).date()
    fixed_date = dt.date(2000, 1, 1)
    old_in_2000_in_days = (fixed_date - date_object).days
    print(f"1.1.2000 sinä olit {old_in_2000_in_days} päivää vanha.")


def print_weekdays():
    test_date = dt.date(2000, 1, 3)
    for _ in range(7):
        print(test_date.strftime("%A"))
        test_date += datetime.timedelta(days=1)     # timedelta to go next day


def print_months():
    test_date = dt.date(2000, 1, 3)
    for _ in range(12):
        print(test_date.strftime("%b"))
        # test_date = test_date + relativedelta(months=+1)    # relative delta to go next month
        test_date += datetime.timedelta(days=31)


def draw_menu():
    print("""Mitä haluat tehdä:
1) Tunnistaa aika-olion komponentit
2) Laskea iän päivinä
3) Tulostaa viikonpäivät
4) Tulostaa kuukaudet
0) Lopeta""")


def main():
    while True:
        draw_menu()
        decision = int(input("Valintasi: "))

        if decision == 1:
            datetime_object = create_datetime_object()
            print()
        elif decision == 2:
            how_old_in_2000()
            print()
        elif decision == 3:
            print_weekdays()
            print()
        elif decision == 4:
            print_months()
            print()
        elif decision == 0:
            break
        else:
            print("Väärä valinta, valitse uudestaan.")


if __name__ == '__main__':
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
    main()
    print("Kiitos ohjelman käytöstä.")
