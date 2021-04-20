from Module23.common_calc_func import calc

summ = 0
with open('calc2.txt', 'r') as file:
    for line in file:
        temp_list = line.split()

        try:
            if len(temp_list) != 3:
                raise ValueError('неполная строка')
            if temp_list[1] not in '+-*%//':
                raise TypeError('неизвестный знак мат действия')
            if not temp_list[0].isdigit() or not temp_list[2].isdigit():
                raise ValueError('в строке есть буквы, а не цифры')
            result = calc(temp_list)
            summ += result

        except ValueError as ve:
            print(ve)
            print('Давайте исправим, сейчас так:', line)
            new_line = input('Введите правильную строку ')
            temp_list = new_line.split()
            print(temp_list)
            result = calc(temp_list)
            summ += result
        except TypeError as te:
            print(te)
            print('Давайте исправим, сейчас так:', line)
            new_line = input('Введите правильную строку ')
            temp_list = new_line.split()
            print(temp_list)
            result = calc(temp_list)
            summ += result
        except ZeroDivisionError:
            print('НА 0 делить нельзя')
            print('Давайте исправим, сейчас так:', line)
            new_line = input('Введите правильную строку ')
            temp_list = new_line.split()
            print(temp_list)
            result = calc(temp_list)
            summ += result
        except FileNotFoundError as fnfe:
            print(fnfe)

print()
print('Финальная сумма всего ', summ)

# TODO дублирование кода нужно избегать
#  добавить проверку исправленной строки
#  иначе выпадет необработанная ошибка
