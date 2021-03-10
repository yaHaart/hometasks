file = open('results.txt', 'r')
winners = dict()
temp_list = []


def new_place(score):
    print('начало определения нового места для ', score)
    temp_list.clear()
    for key, value in winners.items():
        if int(score) > int(value[0]):
            temp_list.append(value[1])
            value[1] += 1
    print('места, которые уже есть ', temp_list)
    if len(temp_list) == 0:
        print('определили место', len(winners) + 1, 'обновленный список', winners)
        return len(winners) + 1
    else:
        print('определили место', max(temp_list), 'обновленный список', winners)
        return min(temp_list)


for line in file:
    name = line.split()[1]
    score = int(line.split()[0])

    if len(winners) == 0:
        winners[name] = [score, 1]
        print('добавлена первая запись', winners)
        print()
        continue

    if name in winners:
        if winners[name][0] < score:
            print(name, '!!!уже есть в списке. Удаляем', winners)
            print('было:', winners[name][0], 'стало:', score)
            place = winners[name][1]
            del winners[name]
            for key, value in winners.items():
                if place <= value[1]:
                    value[1] -= 1
            print('удалил старое и пересчитали места', winners)
            place = new_place(score)
            winners[name] = [score, place]
            print('новый списко', winners)
            print()
    else:
        print(name, 'нет в списке. добавляем', score)
        place = new_place(score)
        winners[name] = [score, place]
        print('новый списко', winners)
        print()
file.close()

print('Таблица победителей в формате Имя, Очки, Место: ', winners)

for i in range(1, len(winners) + 1):
    for winner_key, winner_value in winners.items():
        if winner_value[1] == i:
            print(i, 'место', winner_key, winner_value[0])
