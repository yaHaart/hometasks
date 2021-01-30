violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
new_songs = []
summ = 0
new_list_len = int(input('Сколько песен выбрать? '))
for i in range(new_list_len):
    song = input(f'Название {i + 1} песни: ')
    for j in violator_songs:
        if j[0] == song:
            summ += j[1]
print(round(summ, 2))

# зачёт! 🚀
