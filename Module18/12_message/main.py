line = input(' Введите строку ')
splited_line = line.split()
punctuation_line = '!.,?:;'

punkt_char = ' '
for word in splited_line:
    if word[-1] in punctuation_line:
        punkt_char = word[-1] + ' '
        word = word[:len(word) - 1]
    new_line = ''.join(reversed(word)) + punkt_char
    print(new_line, end='')
    punkt_char = ' '

# TODO нейминг! Исправить названия переменных, записанных транслитом (перевести на английский)
