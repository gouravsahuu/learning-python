list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = []

min_length = min(len(list1), len(list2))

for i in range(min_length):
    list3.append(list1[i] + list2[i])

list3.extend(list1[min_length:])
list3.extend(list2[min_length:])

print(list3)
