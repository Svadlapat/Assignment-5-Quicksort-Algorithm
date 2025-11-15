# randomized_quicksort.py
import random

def randomized_partition(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[rand_pivot], arr[high] = arr[high], arr[rand_pivot]
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


def randomized_quicksort_main(arr):
    randomized_quicksort(arr, 0, len(arr) - 1)
    return arr


# Test
if __name__ == "__main__":
    a = [12, 7, 14, 9, 10]
    print("Original:", a)
    print("Sorted:", randomized_quicksort_main(a))
