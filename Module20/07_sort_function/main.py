origin_tuple = (2, 5, 7, 3, 8, 2, 4.4, 4, 6, 9, 0, 4, 1, 5)


def tuple_sort(some_tuple):
    list_sorted = list(some_tuple)
    list_sorted.sort()
    count = 0
    for number in list_sorted:
        if type(number) is not int:
            count += 1

    if count == 0:
        sorted_tuple = tuple(list_sorted)
        return sorted_tuple
    else:
        return origin_tuple


print(origin_tuple)
print(tuple_sort(origin_tuple))
