db = dict()
n = int(input('Число заказов? '))
for _ in range(n):
    # TODO Лучше сразу разложить данные по переменные - это удобно и индексы тогда будут читаемые.
    #  customer, pizza_name, count = input(f'{_ + 1} заказ: ').split()
    user_input = input('Введите заказ ').split()
    if user_input[0] not in db:
        # TODO dict применять не нужно, простое указание словаря даст тот же эффект
        #  db[user_input[0]] = {user_input[1]: int(user_input[2])}
        db[user_input[0]] = dict({user_input[1]: int(user_input[2])})
    else:
        if user_input[1] not in db[user_input[0]]:
            db[user_input[0]][user_input[1]] = int(user_input[2])
        else:
            db[user_input[0]][user_input[1]] += int(user_input[2])

for key in db.keys():
    print(f'{key:}')
    for second_key, second_value in db[key].items():
        print(f'    {second_key} - {second_value}')

# зачет!
