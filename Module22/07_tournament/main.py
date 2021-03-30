first_tour_players_list = list()
with open('first_tour.txt', 'r', encoding='UTF-8') as first_file:
    min_score = int(first_file.readline())
    for line in first_file:
        first_tour_players_list.append(line.split())

print(first_tour_players_list)

second_tour_players_list = list()
count = 1
for player in first_tour_players_list:
    if int(player[2]) > min_score:
        second_tour_players_list.append([str(count) + ') ' + player[1][:1] + '. ' + player[0], int(player[2])])
        count += 1

sorted_second_tour_players = sorted(second_tour_players_list, key=lambda x: x[1], reverse=True)

with open('second_tour.txt', 'w', encoding='utf-8') as rf:
    pass

with open('second_tour.txt', 'a', encoding='utf-8') as sf:
    sf.write(str(len(sorted_second_tour_players)) + '\n')
    for player in sorted_second_tour_players:
        sf.write(player[0] + ' ' + str(player[1]) + '\n')

# зачёт! 🚀
