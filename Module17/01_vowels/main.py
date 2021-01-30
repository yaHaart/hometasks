vowel_chares = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
line = input('Введите строку ')
vowels_from_line = [char for char in line if char in vowel_chares]
print(vowels_from_line)
print('Длина списка', len(vowels_from_line))
