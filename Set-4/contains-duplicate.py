# **Contains Duplicate**: Given an array of integers, find if the array contains any duplicates.
#     - *Input*: [1, 2, 3, 1]
#     - *Output*: "True"

arr = [1,2,3,1]

def contains_duplicate(arr):
    duplicate = set()
    for num in arr:
        if num in duplicate:
            return True
        duplicate.add(num)
    return False

ans = contains_duplicate(arr)
print(ans)

