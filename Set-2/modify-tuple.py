tuple1 = (11, [22, 33], 44, 55)


new_tuple = list(tuple1)




new_tuple[1][0] = 222


modified_tuple = tuple(new_tuple)

print(modified_tuple)
