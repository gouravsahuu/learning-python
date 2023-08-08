#**Missing Number**: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#     - *Input*: [3, 0, 1]
#     - *Output*: "2"

arr = [3,0,1]

num = 0

arr.sort()

print(arr)

for i in range(0,len(arr)+1) :
    if(arr[i] == num) :
        num += 1
    else :
        print(num)
        break

