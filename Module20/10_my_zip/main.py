line = 'abcd'
# some_iterable_object = [10, 20, 30, 40, 50]
some_iterable_object = (10, 20, 30, 40, 50)
# some_iterable_object = {1: 11, 2: 22, 3: 33, 4: 44, 5: 55}

# new_tuple = zip(line, tuple)
# print(new_tuple)
# for item in new_tuple:
#     print(item)

new_list = list()
for i in range(min(len(line), len(some_iterable_object))):
    new_list.append(tuple([line[i], some_iterable_object[i]]))
print(id(new_list))
print(new_list)






