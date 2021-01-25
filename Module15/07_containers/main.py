number_box = int(input('Кол-во контейнеров: '))
boxes = []
for _ in range(number_box):
    weight = int(input('Введите вес контейнера: '))
    boxes.append(weight)

weight = int(input('Введите вес нового контейнера: '))
counter = 0
while weight <= boxes[counter]:
    counter += 1

print('Номер, куда встанет новый контейнер:', counter + 1)

# зачёт! 🚀
