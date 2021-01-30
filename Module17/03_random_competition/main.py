import random
first_team = [round(random.uniform(5, 10), 2) for x in range(20)]
second_team = [round(random.uniform(5, 10), 2) for x in range(20)]
win_list = [max(first_team[x], second_team[x]) for x in range(20)]
print(first_team)
print(second_team)
print(win_list)
