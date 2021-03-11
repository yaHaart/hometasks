players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
new_list = list()
temp_list = list()
for player in players:
    temp_list.append(player[0])
    temp_list.append(player[1])
    for i in range(3):
        temp_list.append(players[player][i])
    new_list.append(tuple(temp_list))
    temp_list.clear()
print(new_list)

# зачет!
