synonyms_dict = dict()
pare_number = int(input('сколько пар вводить '))
for _ in range(pare_number):
    user_dict = input('Введите пару ').split()
    synonyms_dict[user_dict[0]] = user_dict[1]

while True:
    user_input = input('Введите слово ')
    for key, value in synonyms_dict.items():
        if user_input.lower() == key.lower():
            print('Синоним - ', value)
            break
        elif user_input.lower() == value.lower():
            print('Синоним - ', key)
            break
        else:
            print('Такого слова в словаре нет.')
