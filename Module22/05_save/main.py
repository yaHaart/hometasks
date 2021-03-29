import os.path

text = 'тут какой-то текст для записи'
while True:
    path_input = input('введите путь и имя файла через пробел ').split()
    new_path = '/'
    for part in path_input:
        if part[-4:] != '.txt':
            new_path = os.path.join(new_path, part)
        else:
            file_name = part
    print(new_path)
    if os.path.isdir(new_path):
        break
    else:
        print('такой папки нет в системе ')

if os.path.exists(os.path.join(new_path, file_name)):
    print('файл будет перезаписан')

with open(os.path.join(new_path, file_name), 'w', encoding='UTF-8') as file:
    file.write(text)
