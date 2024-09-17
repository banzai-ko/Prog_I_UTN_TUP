from random import shuffle
import time

# Create a shuffled list of 100,000 elements
lista = list(range(100000))
shuffle(lista)

# Selection Sort implementation
def ordenar_selection_sort(lista: list[int]):
    # Traverse through all list elements
    for i in range(len(lista)):
        # Find the minimum element in the remaining unsorted list
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        lista[i], lista[min_index] = lista[min_index], lista[i]

# Measure the time taken to sort
start_time = time.time()
ordenar_selection_sort(lista)
end_time = time.time()

# Output the time taken
time_taken = end_time - start_time
print("Time taken:", time_taken)
