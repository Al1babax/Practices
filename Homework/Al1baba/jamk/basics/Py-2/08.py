def calculate_grade(points) -> int:
    if points in [10, 11, 12]:
        return 5
    else:
        return points // 2


def main():
    points = int(input("Insert your points: "))
    grade = calculate_grade(points)
    print(f"Grade: {grade}")


if __name__ == '__main__':
    main()
