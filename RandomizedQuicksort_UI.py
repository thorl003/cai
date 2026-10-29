import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        randomized_quicksort(arr, low, p - 1)
        randomized_quicksort(arr, p + 1, high)

arr = list(map(int, input("Enter array elements: ").split()))

print("Original Array:", arr)
randomized_quicksort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)