string = input(' Введите строку ')
numbers_string = ''
for char in string:
    if char.isdigit():
        numbers_string += char

print(numbers_string)
