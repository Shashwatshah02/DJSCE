import random
def randomizedQuickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return randomizedQuickSort(left) + middle + randomizedQuickSort(right)

arr = [1,2,3,4,5,6,7,8,9,0]
print(randomizedQuickSort(arr))