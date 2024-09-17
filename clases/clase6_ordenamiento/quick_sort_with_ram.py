import time
from random import shuffle
from memory_profiler import memory_usage

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

# Function to be used with memory profiler
def sort_and_measure_memory(arr):
    return quick_sort(arr)

if __name__ == '__main__':
    # Create a shuffled list of 500,000 elements
    arr = list(range(50000000))
    shuffle(arr)

    # Measure time and memory
    start_time = time.time()
    mem_usage = memory_usage((sort_and_measure_memory, (arr,)))
    end_time = time.time()

    # Output the time taken and memory usage
    time_taken = end_time - start_time
    print("Time taken:", time_taken)
    print("Memory usage (in MB):", max(mem_usage) - min(mem_usage))
