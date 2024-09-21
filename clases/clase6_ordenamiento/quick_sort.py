import time
from random import shuffle

# Quick Sort function
def quick_sort(arr: list[int]):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr.pop()
        menores = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        mayores = [x for x in arr if x > pivot]
        return quick_sort(menores) + middle + quick_sort(mayores)

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
