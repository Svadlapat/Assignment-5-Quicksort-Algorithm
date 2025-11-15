# analysis.py
import time
import random
import matplotlib.pyplot as plt
from quicksort import quicksort_main
from randomized_quicksort import randomized_quicksort_main

def measure_time(func, arr):
    start = time.time()
    func(arr.copy())
    return time.time() - start


sizes = [1000, 3000, 5000, 7000, 10000]
det_times = []
rand_times = []

for n in sizes:
    print(f"Testing size: {n}")

    # random input
    arr = [random.randint(1, 10000) for _ in range(n)]

    det_times.append(measure_time(quicksort_main, arr))
    rand_times.append(measure_time(randomized_quicksort_main, arr))


# Plotting
plt.plot(sizes, det_times, label="Deterministic Quicksort")
plt.plot(sizes, rand_times, label="Randomized Quicksort")
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Quicksort: Deterministic vs Randomized Performance")
plt.legend()
plt.show()
