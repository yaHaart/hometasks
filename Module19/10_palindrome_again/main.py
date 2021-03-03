line = input('Введите строку: ')
line_dict = dict()
for char in line:
    if char != ' ':
        if char in line_dict:
            line_dict[char] += 1
        else:
            line_dict[char] = 1
summ = 0
for key in line_dict:
    summ += line_dict[key]

poli = True
count = 0
if summ % 2 == 0:
    # print(summ, 'чет')
    for key in line_dict:
        if line_dict[key] % 2 != 0:
            poli = False
else:
    # print(summ, 'нечет')
    for key in line_dict:
        if line_dict[key] % 2 != 0:
            count += 1
    if count != 1:
        poli = False

if poli:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
