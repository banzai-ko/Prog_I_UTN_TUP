import matplotlib.pyplot as plt
import numpy as np
import time

# Function to visualize the array
def visualize_sort(arr, colors):
    plt.bar(range(len(arr)), arr, color=colors)
    plt.pause(0.1)
    plt.clf()

# Selection sort with visualization
def selection_sort_visualized(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # Visualizing the selection of the minimum element
        for j in range(i + 1, n):
            colors = ['blue'] * len(arr)
            colors[i] = 'green'  # Sorted part
            colors[j] = '#1FF497'  # Current element being compa#1FF497
            colors[min_index] = 'yellow'  # Current minimum element
            visualize_sort(arr, colors)

            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # After swapping, visualize the change
        colors = ['blue'] * len(arr)
        colors[i] = 'green'  # Sorted part
        visualize_sort(arr, colors)

    visualize_sort(arr, ['green'] * len(arr))  # Final sorted array
    plt.show()

# Generate random data
arr = np.random.randint(1, 100, 20)

# Setup for visualization
plt.ion()
fig, ax = plt.subplots()
selection_sort_visualized(arr)
plt.ioff()
