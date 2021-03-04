# paires = {
# 'Alexei': 'Peter_I',
# 'Anna': 'Peter_I',
# 'Elizabeth': 'Peter_I',
# 'Peter_II': 'Alexei',
# 'Peter_III': 'Anna',
# 'Paul_I': 'Peter_III',
# 'Alexander_I': 'Paul_I',
# 'Nicholaus_I': 'Paul_I'
# }
pair_number = int(input('Введите количество человек: '))
paires = dict()
for i in range(pair_number - 1):
    pair = input(f'{i + 1} пара ').split()
    paires[pair[0]] = pair[1]
print(paires)

result_dict = dict()
count = 1
flag = False
for kid_name in paires:

    parent = paires[kid_name]
    while not flag:
        # print('внутри вайла родитель', parent)
        if parent in paires:
            # print('да')
            parent = paires[parent]
            count += 1
        else:
            flag = True
            # print('нет')

    # print(kid_name, count)
    result_dict[kid_name] = count
    if count == 1:
        grandparent = paires[kid_name]  # проверкой правильности вводимой структуры данных мы в рамках задачи
        # не заморачиваемся. Считаем, что прародитель есть всегда.
    count = 1
    flag = False
# TODO Переменные созданные в цикле вне цикла использовать нельзя - это может вызывать ошибки.
result_dict[grandparent] = 0

sorted_list_keys = list(result_dict.keys())
sorted_list_keys.sort()
# print(sorted_list_keys)
print('“Высота” каждого члена семьи:')
for i in sorted_list_keys:
    print(i, result_dict[i])
# print(result_dict)

# зачет!
