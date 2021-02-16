line1 = 'asdfgh'
line2 = 'sdfgha'
flag = False
new_line = ''
shift = 0

for i in range(1, len(line1)):
    for j in range(len(line1)):
        new_line += line1[(j + i) % len(line1)]
    if new_line == line2:
        flag = True
        shift = i
        break
    if flag:
        break
    new_line = ''
if flag:
    print('Первая строка получается из второй со сдвигом', shift)
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

# зачёт! 🚀
