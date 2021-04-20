with open('log.txt', 'w', encoding='UTF-8') as log:
    pass

with open('people.txt', 'r', ) as pfile:
    summ = 0
    for line in pfile:
        try:
            length = len(line)
            if line.endswith('\n'):
                length -= 1
            if length > 2:
                summ += length
            else:
                raise TypeError('Длина имени меньше 3 символов')
        except TypeError:
            # print('ошибка в имени')
            with open('log.txt', 'a', encoding='UTF-8') as logfile:
                logfile.write('ошибка длины в имени ' + line )

print('Итоговая сумма', summ)

# зачёт! 🚀
