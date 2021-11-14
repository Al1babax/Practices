def binary_to_dec(b):
    dec = 0
    num_list = [x for x in b]
    for x, num in enumerate(num_list):
        dec += int(num_list[-1 - x]) * (2 ** x)
    print(f"Bittijonosi {b} on kymmenkantaisena kokonaislukuna {dec}")
    return dec


def main():
    binary_number1 = input("Anna ensimmäinen binaariluku: ")
    binary_number2 = input("Anna toinen binaariluku: ")
    a = binary_to_dec(binary_number1)
    b = binary_to_dec(binary_number2)
    c = a - b
    print(f"Lukujen {a} ja {b} erotus on {c}")


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
