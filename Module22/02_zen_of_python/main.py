temp_list = []
with open('zen.txt', 'r', encoding='utf=8') as file:
    temp_list.extend(file.read().split('\n'))

print(temp_list)
for line in reversed(temp_list):
    print(line)

# зачёт! 🚀
