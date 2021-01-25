# простой способ
fraze = input('Введите слово или строку ')
uniq_set = set(fraze)
uniq_set.discard(' ')
print('Кол-во уникальных букв: ', len(uniq_set))

# другой способ
uniq_list = []
for char in fraze:
    if char not in uniq_list and char != ' ':
        uniq_list.append(char)

print('2 Кол-во уникальных букв: ', len(uniq_list))

# зачёт! 🚀
