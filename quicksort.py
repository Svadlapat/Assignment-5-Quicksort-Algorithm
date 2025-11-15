# quicksort.py
def partition(arr, low, high):
    pivot = arr[high]                 # last element as pivot
    i = low - 1                       # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


# Helper wrapper
def quicksort_main(arr):
    quicksort(arr, 0, len(arr) - 1)
    return arr


# Test
if __name__ == "__main__":
    a = [10, 7, 8, 9, 1, 5]
    print("Original:", a)
    print("Sorted:", quicksort_main(a))
