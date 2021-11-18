import urllib.request
import numpy as np
from timeit import default_timer as timer


# urllib.request.urlretrieve("https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv", "climate.txt")

"""arr4 = np.random.randint(0, 10, (5, 5))
arr5 = np.random.randint(0, 10, (5, 5))
arr2 = np.full((5, 5), random.randint(0, 10))
arr3 = np.full((5, 5), 3)"""


def randomize_until_equal_values(equal_values):
    start = timer()
    same_values = 0
    how_many_times = 0
    while same_values != equal_values:
        arr4 = np.random.randint(0, 10, (5, 5))
        arr5 = np.random.randint(0, 10, (5, 5))
        same_values = (arr4 == arr5).sum()
        how_many_times += 1
    end = timer()
    # print(f"Tän paskan piti mennä {how_many_times} kertaa")
    return end - start


def average_runtime(equal_values, times):
    value_time_list = []
    for _ in range(times):
        runtime = randomize_until_equal_values(equal_values)
        value_time_list.append(runtime)
        # print(f"Finding {equal_values} equal values in array size of 5x5 with values in random from 0 to 10"
        #   f" with sample size of {times} took in average {sum(value_time_list)} seconds")
    return sum(value_time_list)


def get_data():
    data = []  # (equal_values, average_runtime)
    for x in range(9):
        runtime = average_runtime(x + 1, 100)
        data.append((x + 1, runtime))
        print(f"Progress done {round(((x + 1) / 9) * 100, 2)}%")
    return data


def main():
    main_data = get_data()
    data_array = np.array(main_data)
    np.savetxt("runtime_results.txt", data_array, header="equal_numbers time(seconds)", comments="")


if __name__ == '__main__':
    main()
