n_people = 5
count_out = 3
people = list(range(1, n_people + 1, 1))
start_count = 0
for _ in range(n_people - 1):
    print('Текущий круг людей: ', people)
    print('Начало счёта с номера ', people[start_count])
    i_out = (start_count - 1 + count_out)
    while i_out >= len(people):
        i_out = i_out - len(people)

    print('Выбывает человек под номером', people[i_out])
    del people[i_out]
    if i_out == len(people):
        start_count = 0
    else:
        start_count = i_out
    print()

print('Остался человек под номером ', people[0])
