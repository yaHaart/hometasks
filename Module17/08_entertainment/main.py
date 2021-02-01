import random
sticks = int(input('Кол-во палок:  '))
shots = int(input('Кол-во бросков: '))
shots_numbers = []
for j in range(shots):
    k1 = random.randint(1, sticks)
    k2 = random.randint(1, sticks)
    print(f'Бросок {j + 1}. Сбиты палки с номера {min(k1, k2)} по номер {max(k1,k2)}')
    for i in range(min(k1, k2), max(k1,k2) + 1):
        shots_numbers.append(i)
shots_numbers_unic = set(shots_numbers)
sticks_out = [('.' if x in shots_numbers_unic else '!') for x in range(1, sticks + 1)]
for x in sticks_out:
    print(x, end='')

# зачёт! 🚀
