def revers_string(message):
    return message == message[::-1]  # так тоже можно


line = input('Введите слово ')
flag = revers_string(line)
if flag:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

# зачёт! 🚀
