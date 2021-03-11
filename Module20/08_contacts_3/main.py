db = {
    ('Сидоров', 'Никита'): '+79873434125',
    ('сидорова', 'Алина'): '+79873434154',
    ('Сидоров', 'Павел'): '+79873436935',
    ('Иванов', 'Иван'): '+79836814125'
}


def surname_find(surname):
    for human in db:
        if human[0].lower().find(surname.lower()) >= 0:
            print(human[0], human[1], db[human])
    print()


def new_human(surname, name, telephone):
    tuple_index = tuple([surname, name])
    if tuple_index in db:
        print('Обновил номер телефона для', tuple_index)
        db[tuple_index] = telephone
    else:
        print('Контакт добавлен')
        db[tuple_index] = telephone
        for human in db:
            print(human, db[human])
    print()


while True:
    print('Выход - 0')
    print('Поиск по фамилии - 1')
    action = int(input('Добавить контакт - 2 '))
    print()
    if action == 1:
        surname = input('Введите фамилию ')
        surname_find(surname)
    elif action == 2:
        surname = input('Введите фамилию ')
        name = input('Введите имя ')
        telephone = input('Введите номер телефона ')
        new_human(surname, name, telephone)
    else:
        break

# зачет!
