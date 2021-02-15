line = input(' Введите строку ')
splited_line = line.split()
punctuation_line = '!.,?:;'

punktuation_char = ' '
for word in splited_line:
    if word[-1] in punctuation_line:
        punktuation_char = word[-1] + ' '
        word = word[:len(word) - 1]
    new_line = ''.join(reversed(word)) + punktuation_char
    print(new_line, end='')
    punktuation_char = ' '


