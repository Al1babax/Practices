import datetime as dt
import sys


def yearly_car_amount(file_list) -> dict:
    car_yearly_dict = {}
    for car_info in file_list:
        date = dt.datetime.strptime(car_info[1], "%Y-%m-%d")
        if date.year not in car_yearly_dict:
            car_yearly_dict[date.year] = 1
        else:
            car_yearly_dict[date.year] += 1
    car_yearly_dict = dict(sorted(car_yearly_dict.items(), key=lambda x: x[0], reverse=True))
    return car_yearly_dict


def read_file(file_name):
    try:
        file_list = []
        with open(file_name) as f:
            for line in f.readlines():
                file_list.append(line[:-1].split(";"))
            file_list.pop(0)
        return file_list
    except FileNotFoundError:
        print(f"Tiedoston '{file_name}' avaaminen epäonnistui.")
        sys.exit()


def print_data(car_yearly_dict):
    print("Autot lajiteltuna vuosiluvun mukaan laskevaan järjestykseen.")
    print("Vuosi: Autoja")
    for year, amount in car_yearly_dict.items():
        print(f"{year}: {amount}")
    print(f"Yhteensä {sum(car_yearly_dict.values())} autoa.")


def main():
    file_name = input("Anna luettavan tiedoston nimi: ")
    # file_name = "L10T3Data.txt"
    file_list = read_file(file_name)
    # print(file_list)
    car_yearly_dict = yearly_car_amount(file_list)
    # print(car_yearly_dict)
    print_data(car_yearly_dict)


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
