#randomized quick sort

import random
import time

c1, c2 = 0, 0

def randomized_quicksort(arr):
    global c2
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        c2 += len(left) + len(right)
        return randomized_quicksort(left) + middle + randomized_quicksort(right)

def quicksort(arr):
    global c1
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        c1 += len(left) + len(right)
        return quicksort(left) + [pivot] + quicksort(right)

arr = [random.randint(0, 100) for i in range(100)]
arr1 = arr.copy()

st = time.time()

print("-----------------------------------------------------------------------------------------")
print("Sorted by normal way :", quicksort(arr1))
print("Time taken by normal quicksort:", (time.time() - st), "\nComparisons:", c1)

st = time.time()

print("-----------------------------------------------------------------------------------------")
print("Sorted by randomized way :", randomized_quicksort(arr))
print("Time taken by randomized quicksort:", (time.time() - st), "\nComparisons:", c2)

print("-----------------------------------------------------------------------------------------")
