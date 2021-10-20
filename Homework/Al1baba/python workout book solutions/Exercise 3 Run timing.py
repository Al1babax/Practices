"""
Idea is to make a data tracking software that gives some information about that data
Important to remember that floats are not 100% accurate, use module like decimal to use accurate math!
"""
import decimal
from decimal import *


def run_timing():
    run_times = []
    new_time = True
    x = 0

    while new_time:
        run_times.append(input("Enter 10km run time: "))

        if run_times[x] == "":
            run_times.pop(x)
            new_time = False
            # Making sure every item in the list are floats
            for x in range(len(run_times)):
                run_times[x] = float(run_times[x])

            average = round((sum(run_times) / (x + 1)), 2)
            print(f"Average of {average}, over {x + 1} runs")

        x += 1


# run_timing()

print(0.1 + 0.2)

# Making a function that can calculate accurate decimal points


def decimal_function(num1, num2):
    num1 = decimal.Decimal(num1)
    num2 = decimal.Decimal(num2)

    result = float(num1 + num2)

    print(result)


#decimal_function("0.1", "0.2")
