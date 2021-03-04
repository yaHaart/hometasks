violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

number_songs = 3
summ = 0
for i_song in range(number_songs):
    user_song = input(f'Введите название {i_song + 1} песни ')
    if user_song in violator_songs:
        summ += violator_songs[user_song]
    else:
        print('Нет такой песни')

print(f'Общее время звучания песен: {summ} минут')

# зачет!
