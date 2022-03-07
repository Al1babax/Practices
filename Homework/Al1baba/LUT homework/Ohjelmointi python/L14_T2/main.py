import urllib.request
import re
import xml.etree


def read_website(url) -> list:
    with urllib.request.urlopen(url) as f:
        source_code = []
        for line in f.readlines():
            source_code.append(str(line)[2:-1])
    return source_code


def clean_data(data) -> list:  # Apparently this is not working for all lines
    cleaner = re.compile(r'<[^>]+>')
    for x in range(len(data)):
        data[x] = cleaner.sub("", data[x])
    return data


def clean_data3(data):
    appending_mode_bool = True
    output_list = []
    output_str = ""

    for line in data:
        for char_str in line:
            if char_str == '<':
                appending_mode_bool = False
            elif char_str == '>':
                appending_mode_bool = True
                continue
            if appending_mode_bool:
                output_str += char_str
        output_list.append(output_str)
        output_str = ""

    return output_list


def write_data(data):
    with open("htulos.txt", "w+") as f:
        for x, line in enumerate(data):
            # print(line[:3])
            if line[-2:] == "\\n" and line[:2] == "\\t":
                f.write(f"\t{line[2:-2]}\n")
            elif line[-2:] == "\\n":
                f.write(f"{line[:-2]}\n")


def main():
    url = 'http://saja.kapsi.fi/var_roles/role_list.html'
    data = read_website(url)
    # for line in data:
     #    print(line)
    cleaned_data = clean_data3(data)
    # print(data)
    # print(cleaned_data)
    write_data(cleaned_data)


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
