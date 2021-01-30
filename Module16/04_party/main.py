guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
action = ''
while action != 'пора спать':
    print(f'Сейчас на вечеринке {len(guests)} человек:', guests)
    action = input('Гость пришёл или ушёл? ')
    if action == 'пришел' and len(guests) < 6:
        guest_name = input('Имя гостя: ')
        guests.append(guest_name)
    elif action == 'пришел' and len(guests) >= 6:
        guest_name = input('Имя гостя: ')
        print(f'Прости, {guest_name}, но мест нет.')
    elif action == 'ушел':
        guest_name = input('Имя гостя: ')
        if guest_name in guests:
            guests.remove(guest_name)
        else:
            print('Нет такого гостя ')
    else:
        print('не знаю такой команды')

print('Вечеринка закончилась, все легли спать.')

# зачёт! 🚀
