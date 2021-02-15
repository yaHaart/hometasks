string = input('Введите строку ')
zip_str = ''
count = 0
for i in range(1, len(string)):  # TODO гораздо проще задать интервал range(len(string))
    count += 1
    if string[i - 1] != string[i]:
        zip_str += (string[i - 1] + str(count))
        count = 0
    elif i == len(string) - 1:
        zip_str += (string[i - 1] + str(count + 1))


print('закодированная строка ', zip_str)
# TODO последний символ не попал в закодированный ответ:
#  Введите строку aaAAbbсaaaA
#  закодированная строка  a2A2b2с1a3
#  .
#  Должно получиться:
#  Закодированная строка: a2A2b2a3A1
