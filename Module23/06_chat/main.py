
import time
db = {}


def username():
    temp_list = []
    set_user = set()
    if len(db) > 0:
        for key, value in db.items():
            temp_list.append(value[0])
        set_user = set(temp_list)
    temp_dict = {x: set_user[x] for x in range(len(set_user))}
    print(temp_dict)
    return input('Кто говорит? ')


print('Управление: *** смена пользователя')
print('            @@@ завершение чата')
current_user = ''
while True:
    if current_user == '':
        current_user = username()
    user_input = input()
    if user_input == '***':
        current_user = username()
    elif user_input == '@@@':
        break
    else:
        # current_time = datetime.datetime.now().strftime('%H.%M.%S')
        current_time = time.time()
        db[current_time] = [current_user, user_input]

print(db)

# NOTE 1) смена пользователя работает некорректно (выдаёт ошибку TypeError: 'set' object is not subscriptable)
# 2) формат даты лучше использовать понятный человеку:
#  {1619182769.2150478: ['qwew qwe', 'qwe'], 1619182769.7676811: ['qwew qwe', 'ewq']}
