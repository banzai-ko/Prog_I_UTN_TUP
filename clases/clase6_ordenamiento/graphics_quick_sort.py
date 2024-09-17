import matplotlib.pyplot as plt
import numpy as np

def quicksort(arr, low, high, ax, step):
    if low < high:
        p = partition(arr, low, high, ax, step)
        quicksort(arr, low, p - 1, ax, step)
        quicksort(arr, p + 1, high, ax, step)

def partition(arr, low, high, ax, step):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            plot_array(arr, ax, step, pivot_index=j)
            step[0] += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    plot_array(arr, ax, step, pivot_index=i + 1)
    step[0] += 1
    return i + 1

def plot_array(arr, ax, step, pivot_index=None):
    ax.clear()
    colors = ['#1FF497' if i == pivot_index else 'blue' for i in range(len(arr))]
    ax.bar(range(len(arr)), arr, color=colors)
    ax.set_title(f'Step {step[0]}')
    plt.pause(0.5)

def quicksort_visualize(arr):
    fig, ax = plt.subplots()
    step = [0]
    plot_array(arr, ax, step)
    quicksort(arr, 0, len(arr) - 1, ax, step)
    plt.show()

# Example usage
arr = [9, 3, 8, 10, 2, 5, 1, 7, 6, 4]
quicksort_visualize(arr)
