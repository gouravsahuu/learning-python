# **Bubble Sort**: Implement the bubble sort algorithm in Python.
#     - *Input*: [64, 34, 25, 12, 22, 11, 90]
#     - *Output*: "[11, 12, 22, 25, 34, 64, 90]"

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

list1 = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(list1)

print(list1)
