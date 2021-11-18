"""
I could make each data entry their own object with name, age, phone number. But since I have so little data and small
program I decided to go this way::: The whole file is a object
"""
import sys


class File:

    def __init__(self, file):
        try:
            with open(file) as f:
                file_data = []
                for line in f.readlines():
                    file_data.append(line[:-1])
                self.data = file_data
        except FileNotFoundError:
            print(f"Tiedoston '{file}' avaaminen epäonnistui.")
            sys.exit()

    def print_file(self):
        for element in self.data:
            temp_line = element.split(";")
            print(f"{temp_line[0]} on {temp_line[2]} vuotta vanha ja hänen puhelinnumero on {temp_line[1]}.")

    def write_file(self):
        age_threshold = int(input("Minkä ikäiset ihmiset otetaan mukaan tiedostoon (vuosia): "))
        number_of_people = 0
        with open("tulos.txt", "w+") as f:
            for line in self.data:
                if int(line[-2:]) >= age_threshold:
                    f.write(f"{line}\n")
                    number_of_people += 1
        with open("tulos.txt", "r+") as a:
            content = a.read()
            a.seek(0, 0)
            a.write(f"Tiedostossa on mukana {number_of_people} vähintään {age_threshold} vuotiasta henkilöä:\n")
            a.write(content)


if __name__ == '__main__':
    pass
