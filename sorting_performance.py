import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Function to measure sorting time
def measure_time(sort_function, arr):
    start_time = time.time()
    if sort_function == quick_sort:
        sort_function(arr.copy())  # Quick sort returns a new list
    else:
        sort_function(arr)  # Bubble and Merge sort modify in-place
    return time.time() - start_time

# Generate random dataset (simulating stock prices)
size = 500  # Adjust for different scales
data = np.random.randint(1, 10000, size)

# Measuring sorting times
results = {
    "Bubble Sort": measure_time(bubble_sort, data.copy()),
    "Quick Sort": measure_time(quick_sort, data.copy()),
    "Merge Sort": measure_time(merge_sort, data.copy())
}

# Convert to DataFrame and print results
df_results = pd.DataFrame(list(results.items()), columns=["Algorithm", "Time (s)"])
print(df_results)

# Plot results
plt.figure(figsize=(8, 5))
plt.bar(results.keys(), results.values(), color=['blue', 'green', 'red'])
plt.xlabel("Sorting Algorithm")
plt.ylabel("Time Taken (seconds)")
plt.title("Sorting Algorithm Performance Comparison")
plt.savefig("sorting_results.png", dpi=300, bbox_inches='tight')
plt.show()
