# не понял условие задачи. data - это число. считаем мы все один раз. что и как не нужно пересчитывать?

def calculating_math_func(data):
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    return result


print(calculating_math_func(10))
