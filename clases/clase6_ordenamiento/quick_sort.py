import time
from random import shuffle

# Quick Sort function
def quick_sort(arr: list[int]):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Create a shuffled list of 100,000 elements
arr = list(range(500000))
shuffle(arr)

# Measure time
start_time = time.time()
sorted_arr = quick_sort(arr)
end_time = time.time()

# Output the time taken
time_taken = end_time - start_time
print("Time taken:", time_taken)
