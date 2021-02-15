string = input('Введите строку ')
zip_str = ''
count = 0
for i in range(len(string)):
    count += 1
    print(i)
    if i == len(string) - 1:
        zip_str += (string[i] + str(count))
        print('последний символ')
    elif string[i] != string[i + 1]:
        zip_str += (string[i] + str(count))
        print('непоследний')
        count = 0

print('закодированная строка ', zip_str)
