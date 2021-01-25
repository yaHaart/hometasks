films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favorites_films = []
flag = True
while flag:
    film = input(' Введите любимый фильм. Для окончания ввода введите пустую строку ')
    if film in films:
        favorites_films.append(film)
        print('Добавлен ')
    elif film not in films and film != '':
        print('не знаю такого фильма ')
    else:
        flag = False

print('Любимые фильмы', favorites_films)

# TODO сейчас допустима ситуация с сохранением дубликатов: ['Мементо', 'Мементо', 'Мементо']
