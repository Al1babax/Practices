def main():
    grades = []
    grade = 0

    while grade != "":
        grade = input("Give new grade(Press Enter to stop): ")
        if grade != "":
            grades.append(int(grade))

    print(f"You gave {len(grades)} grades and their average is {round(sum(grades) / len(grades), 2)}")


if __name__ == '__main__':
    main()
