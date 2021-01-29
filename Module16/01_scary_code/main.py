a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
a_count = a.count(5)
print('Кол-во цифр 5 при первом объединении: ', a_count)
for _ in range(a_count):
    a.remove(5)
a.extend(c)
c_count = a.count(3)
print('Кол-во цифр 3 при втором объединении: ', c_count)
print('Итоговый список: ', a)
