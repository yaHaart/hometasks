russian_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                   'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

line = input('Введите строку ')
k = int(input('Сдвиг '))
new_line = [(russian_letters[russian_letters.index(letter) + k - 33] if letter != ' ' else ' ') for letter in line]

for char in new_line:
    print(char, end='')

print()

# зачёт! 🚀
