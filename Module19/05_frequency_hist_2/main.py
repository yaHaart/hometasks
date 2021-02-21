line = 'Тут туту поезд'
init_dict = dict()
revers_dict = dict()
temp = []

for char in line:
    if char in init_dict:
        init_dict[char] += 1
    else:
        init_dict[char] = 1

print(init_dict)

for key, value in init_dict.items():
    if value in revers_dict:
        revers_dict[value].append(key)
    else:
        revers_dict[value] = list(key)

print(revers_dict)
