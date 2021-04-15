summ = 0
with open('calc.txt', 'r') as file:
    for line in file:
        temp_list = line.split()

        try:
            if len(temp_list) != 3:
                raise ValueError('неполная строка')
            if temp_list[1] not in '+-*%//':
                raise TypeError('неизвестный знак мат действия')
            if not temp_list[0].isdigit() or not temp_list[2].isdigit():
                raise ValueError('в строке есть буквы, а не цифры')

            if temp_list[1] == '+':
                summ += int(temp_list[0]) + int(temp_list[2])
            elif temp_list[1] == '-':
                summ += int(temp_list[0]) - int(temp_list[2])
            elif temp_list[1] == '*':
                summ += int(temp_list[0]) * int(temp_list[2])
            elif temp_list[1] == '//':
                summ += int(temp_list[0]) // int(temp_list[2])
            elif temp_list[1] == '%':
                summ += int(temp_list[0]) % int(temp_list[2])
            elif temp_list[1] == '/':
                summ += int(temp_list[0]) / int(temp_list[2])
            else:
                raise TypeError('Что-то пошло не так. Скорее всего я не знаю такой знак')

        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
        except ZeroDivisionError:
            print('НА 0 делить нельзя')

print()
print('Финальная сумма всего ', summ)
