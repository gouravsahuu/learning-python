# 15. **Single Number**: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#     - *Input*: [4,1,2,1,2]
#     - *Output*: "4"

arr = [1,2,3,1,3,2,4]

obj = {}

for num in arr:
    if num not in obj:
        obj[num] = 1
    else:
        obj[num] += 1

ans = None
for key, value in obj.items():
    if value == 1:
        ans = key
        break

print(ans)


