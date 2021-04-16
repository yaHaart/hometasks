def calc(temp_list):
    if temp_list[1] == '+':
        summa = int(temp_list[0]) + int(temp_list[2])
    elif temp_list[1] == '-':
        summa = int(temp_list[0]) - int(temp_list[2])
    elif temp_list[1] == '*':
        summa = int(temp_list[0]) * int(temp_list[2])
    elif temp_list[1] == '//':
        summa = int(temp_list[0]) // int(temp_list[2])
    elif temp_list[1] == '%':
        summa = int(temp_list[0]) % int(temp_list[2])
    elif temp_list[1] == '/':
        summa = int(temp_list[0]) / int(temp_list[2])
    else:
        raise TypeError('Что-то пошло не так. Скорее всего я не знаю такой знак')
    return summa