list1 = []
list2 = []
for _ in range(3):
    input_fig = int(input('Введите число первого списка '))
    list1.append(input_fig)
for _ in range(7):
    input_fig = int(input('Введите число второго списка '))
    list2.append(input_fig)

print(list1, list2)
list1.extend(list2)


# способ 1
list3 = list(set(list1))
print('Новый первый список с уникальными элементами способ 1', list3)

# способ 2
i = 0
while i < len(list1):
    figure = list1[0]
    for j in range(list1.count(figure)):
        list1.remove(figure)
    list1.append(figure)
    i += 1
print('Новый первый список с уникальными элементами способ 2', list1)

# зачёт! 🚀
