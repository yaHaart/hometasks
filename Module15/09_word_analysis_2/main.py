def revers_string(message):
    if message == message[::-1]:
        return True
    else:
        return False


line = input('Введите слово ')
flag = revers_string(line)
if flag:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
