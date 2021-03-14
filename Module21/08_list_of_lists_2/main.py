nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

new_list = []


def in_list(structure):
    for elem_in_func in structure:
        if isinstance(elem_in_func, list):
            in_list(elem_in_func)
        else:
            new_list.append(elem_in_func)


for element in nice_list:
    if isinstance(element, list):
        in_list(element)
    else:
        new_list.append(element)

print(new_list)
