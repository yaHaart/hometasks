skates_list = []
men_list = []
n = int(input('Кол-во коньков: '))
for i in range(n):
    skate = int(input(f'Размер {i + 1} пары: '))
    skates_list.append(skate)

m = int(input('Кол-во людей: '))
for i in range(n):
    men = int(input(f'Размер ноги {i + 1} человека: '))
    men_list.append(men)

skates_list.sort()
men_list.sort()

count = 0
for i in range(len(men_list)):
    for j in range(len(skates_list)):
        if men_list[i] <= skates_list[j]:
            count += 1
            del skates_list[j]
            break

print('Наибольшее кол-во людей, которые могут взять ролики: ', count)

# зачёт! 🚀
