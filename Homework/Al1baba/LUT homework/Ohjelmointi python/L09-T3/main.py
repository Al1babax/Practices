import sys


def read_file(file_name):
    data_list = []
    lines_data = {}
    try:
        with open(file_name) as f:
            for line in f.readlines():
                data_list.append(line[:-1])
            for line_number, line in enumerate(data_list):
                lines_data[line_number + 1] = line.split(";")
        return lines_data
    except FileNotFoundError:
        print(f"Tiedoston '{file_name}' avaaminen epäonnistui.")
        sys.exit(0)



def test_file(random_parameter):
    print(f"Aliohjelman parametrina tuli {random_parameter}")
    file = input("Anna tiedostonimi: ")
    data = read_file(file)

    for key, value in data.items():
        # print(key)
        # print(value)
        try:
            new_value = float(value[0]) / float(value[1])
            new_value += random_parameter
            print(f"Rivi {key}: Summa on {new_value:0.2f}.")
        except ZeroDivisionError:
            print(f"Rivi {key}: Nollalla ei voi jakaa.")
        except ValueError:
            print(f"Rivi {key}: Rivillä ei ollut numerodataa.")
        except IndexError:
            print(f"Rivi {key}: Rivillä ei ole riittävästi lukuja.")
        except TypeError:
            print(f"Rivi {key}: Parametri oli väärää tietotyyppiä.")
            sys.exit(0)


def main():
    test_parameters = [10.0, "abc"]
    for x in range(len(test_parameters)):
        test_file(test_parameters[x])


if __name__ == '__main__':
    main()
