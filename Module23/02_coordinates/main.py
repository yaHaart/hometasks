import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


with open('result.txt', 'w') as file:
    pass

try:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            # print(nums_list)
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            with open('result.txt', 'a') as file_2:
                my_list = sorted([res1, res2, number])
                file_2.write(' '.join(str(my_list)) + '\n')

except Exception:
    print("Что-то пошло не так")
except ZeroDivisionError:
    print('Случайно поделили на 0')

# TODO сейчас в ответы попадают лишние знаки пробелов:
# [ 1 . 2 5 ,   2 . 7 5 ,   5 3 ]
# [ - 0 . 4 ,   1 . 0 ,   1 8 ]
# [ 0 . 0 ,   2 . 0 ,   5 0 ]
# [ 0 . 8 0 2 4 6 9 1 3 5 8 0 2 4 6 9 1 ,   1 . 4 1 1 7 6 4 7 0 5 8 8 2 3 5 3 ,   1 3 ]
# [ 1 . 5 8 3 3 3 3 3 3 3 3 3 3 3 3 3 3 ,   1 . 6 ,   1 6 ]
# TODO такие данные в дальнейшем обрабатывать будет сложнее, если бы изначально они сохранились верно
