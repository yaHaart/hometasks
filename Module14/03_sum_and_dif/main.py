def summ_digit(n):
    line = str(n)
    summ = 0
    for char in line:
        summ += int(char)
    return summ


def length(n):
    length = len(str(n))
    return length


n = int(input('Введите число: '))
summ = summ_digit(n)
length = length(n)
print('Сумма чисел:', summ)
print('Кол-во цифр в числе: ', length)
print('Разность суммы и кол-ва цифр:', summ - length)

# зачёт! 🚀
