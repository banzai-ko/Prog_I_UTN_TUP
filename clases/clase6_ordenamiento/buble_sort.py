from random import shuffle
import time
lista =  list(range(10000))

shuffle(lista)
# print("Original listay:", lista) 

def bubble_sort(list):
    n = len(list)
    # Traverse through all elements in the lista
    for i in range(n):
        # Flag to check if any swapping occurs
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the listay from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True
        # If no swapping happens, the listay is already sorted
        if not swapped:
            break
start_time = time.time()
bubble_sort(lista)
end_time = time.time()
time_taken = end_time - start_time

print("Time taken:", time_taken)