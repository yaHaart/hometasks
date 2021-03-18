some_list = [1, 3, 6, 8, 3, [1, 3, [1, 2, 2], 5, 5]]


def summ(structure):
    summa_in_func = 0
    for element_in_func in structure:
        if isinstance(element_in_func, list):
            summa_in_func += summ(element_in_func)
        else:
            summa_in_func += element_in_func
    return summa_in_func


summa = summ(some_list)

print(summa)
