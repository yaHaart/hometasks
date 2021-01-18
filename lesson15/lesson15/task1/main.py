n = int(input('Введите число '))
odd_list = []
for i in range(1, n + 1):
    if i % 2 != 0:
        odd_list.append(i)

print(odd_list)
