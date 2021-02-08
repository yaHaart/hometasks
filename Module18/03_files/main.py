bad_simbols = '@№\$%^&*()'
string = input('Введите название файла: ')

if not string.endswith('.txt') and not string.endswith('.doc'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
elif string[0] in bad_simbols:
    print('Ошибка: название начинается на один из специальных символов')
else:
    print('Файл назван верно.')
