db = dict()
n = int(input('Число заказов? '))
for _ in range(n):
    user_input = input('Введите заказ ').split()
    if user_input[0] not in db:
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
