base_list = [1, 2, 3, 4, 5]
new_list = []
k = int(input('Сдвиг: '))

while k > len(base_list):
    k -= len(base_list)

for i in range(len(base_list)):
    new_list.append(base_list[i - k])

print('Изначальный список: ', base_list)
print('Сдвинутый список: ', new_list)

# зачёт! 🚀
