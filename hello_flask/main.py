import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def fast_function():
    for i in range(1000000):
        i * i


def slow_function():
    for i in range(10000000):
        i * i


def speed_calc_decorator():
    current_time_fast = time.time()
    fast_function()
    new_current_time = time.time()
    time_diff_fast = new_current_time - current_time_fast

    current_time_slow = time.time()
    slow_function()
    new_current_time_slow = time.time()
    time_diff_slow = new_current_time_slow - current_time_slow

    print(f"fast_fucntion run speed: {time_diff_fast}s")
    print(f"slow_fucntion run speed: {time_diff_slow}s")


speed_calc_decorator()
