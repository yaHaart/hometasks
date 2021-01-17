def revers_number(number):
    line = str(number)
    a = line.split('.')
    new_line = ''
    new_line = a[0][::-1] + '.' + a[1][::-1]
    return float(new_line)


number1 = float(input('Введите первое число: '))
number2 = float(input('Введите второе число: '))

rev_num1 = revers_number(number1)
rev_num2 = revers_number(number2)
print('Первое число наоборот: ', rev_num1)
print('Второе число наоборот: ', rev_num2)
print('Сумма: ', rev_num1 + rev_num2)

