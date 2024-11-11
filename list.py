#empty list
my_list = []

# append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Sinsert values
my_list.insert(1, 15)

# extend to another list
my_list.extend([50, 60, 70])

# remove from list
my_list.pop()

# sort
my_list.sort()

# print
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
#print
print("Final list:", my_list)
