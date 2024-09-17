import matplotlib.pyplot as plt
import numpy as np
import time

# Function to visualize the array
def visualize_sort(arr, colors):
    plt.bar(range(len(arr)), arr, color=colors)
    plt.pause(0.1)
    plt.clf()

# Bubble sort with visualization
def bubble_sort_visualized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Visualize the current state
            colors = ['blue'] * len(arr)
            colors[j] = '#1FF497'
            colors[j + 1] = '#1FF497'
            visualize_sort(arr, colors)
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    visualize_sort(arr, ['green'] * len(arr))  # Final sorted array in green
    plt.show()

# Generate random data
arr = np.random.randint(1, 100, 20)

# Setup for visualization
plt.ion()
fig, ax = plt.subplots()
bubble_sort_visualized(arr)
plt.ioff()
