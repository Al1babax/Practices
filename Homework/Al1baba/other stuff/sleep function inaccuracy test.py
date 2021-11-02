"""
Checking delay for sleep function
"""
import time

time_list = []


def measure_time(func):
    def wrapper(*arg):
        t = time.time()
        res = func(*arg)
        # print("Function took " + str(time.time() - t) + " seconds to run")
        total_t = time.time() - t
        return res, total_t

    return wrapper


@measure_time
def my_function(n):
    time.sleep(n)


def check_delay(sleep_duration):
    global time_list

    for x in range(10):
        time_list.append((my_function(sleep_duration)[1] - sleep_duration) * 1000)

    average_delay = sum(time_list) / len(time_list)

    print(f"""
    Times in milliseconds:
    Sleep duration {sleep_duration * 1000}

    All the delays: {time_list}
    Highest delay: {max(time_list)} milliseconds
    Lowest delay: {min(time_list)} milliseconds
    Average delay: {average_delay} milliseconds
    Average inaccuracy: {(round(average_delay / (sleep_duration * 1000), 3)) * 100} %
    """)
    time_list = []


check_delay(1e-05)
check_delay(1e-04)
check_delay(1e-03)
check_delay(1e-02)
check_delay(0.1)
check_delay(1)
