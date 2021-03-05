origin_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = list()
temp_list = list()
new_list1 = list()

for i in range(0, len(origin_list), 2):
    temp_list.append(origin_list[i])
    temp_list.append(origin_list[i + 1])
    new_list.append(tuple(temp_list))
    temp_list.clear()

print(new_list)

for i in range(0, len(origin_list), 2):
    new_list1.append(tuple([origin_list[i], origin_list[i + 1]]))
print(new_list1)
