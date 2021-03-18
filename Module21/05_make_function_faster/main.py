from random import randint
factorials = {}


def calculating_math_func(start, data, result):
    for index in range(start, data + 1):
        result *= index
        factorials[index] = result


for _ in range(5):
    argument = randint(3, 7)
    if len(factorials) == 0:
        calculating_math_func(1, argument, 1)
        math_result = factorials[argument]
    elif argument in factorials:
        math_result = factorials[argument]
    else:

        max_factorial = len(factorials)
        calculating_math_func(max_factorial + 1, argument, factorials[max_factorial])
        math_result = factorials[argument]

    math_result /= math_result ** 3
    math_result = math_result ** 10
    print(argument, math_result)
