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
                file_2.write(''.join(str(my_list)) + '\n')

except Exception:
    print("Что-то пошло не так")
except ZeroDivisionError:
    print('Случайно поделили на 0')

# зачёт! 🚀
