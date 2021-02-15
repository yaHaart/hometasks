upper_chars = 0
numbers = 0
while True:
    string = input('введите пароль: ')
    for char in string:
        if char.isupper():
            upper_chars += 1
        if char.isdigit():
            numbers += 1
    if upper_chars < 1 or numbers < 3 or len(string) < 8:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break  # так тоже можно ;)
        # NOTE лучше в коде не создавать переменных, без которых можно легко обойтись

# зачёт! 🚀
