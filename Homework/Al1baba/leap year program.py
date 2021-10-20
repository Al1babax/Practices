# Making a program that takes 2 variables and checks if there are leap years between those years


def leap_checker (num1, num2):

    first_year = num1

    for year in range(num2 - num1):

        if (first_year % 4) != 0:
            pass

        elif (first_year % 100) != 0:
            print(f"Year {first_year} is a leap year")

        elif (first_year % 400) != 0:
            pass

        else:
            print(f"Year {first_year} is a leap year")
            pass
        first_year += 1



leap_checker(1996, 2021)