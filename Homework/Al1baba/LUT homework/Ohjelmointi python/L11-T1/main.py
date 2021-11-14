def find_square_root(num1):
    square_root = 0
    lower_square_value = 0
    higher_square_value = 0
    if num1 == 0:
        return 0
    elif num1 == 1:
        return 1

    for x in range(num1):
        current_square_root_value = x ** 2
        if current_square_root_value > num1:
            higher_square_value = current_square_root_value
            break
        elif current_square_root_value < num1 or current_square_root_value == num1:
            square_root = x
            lower_square_value = current_square_root_value

    a = num1 - lower_square_value
    if a == 0:
        return square_root
    if a / (higher_square_value - lower_square_value) >= 0.5:
        square_root += 1

    return square_root


def main():
    num1 = int(input("Anna luku: "))
    square_root = 0
    """
    for x in range(50000):
        num1 = x
        square_root = find_square_root(num1)
        print(f"Neliöjuuri on {square_root}")
    """
    square_root = find_square_root(num1)
    print(f"Neliöjuuri on {square_root}")


if __name__ == '__main__':
    main()
