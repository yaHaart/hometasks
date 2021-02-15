line = input('введите пример для решения. Ограничение - вложенные скобки ')


def addition(additional_line):
    summ = int(additional_line[0])
    for i_add in range(1, len(additional_line), 2):
        if additional_line[i_add] == '+':
            summ += int(additional_line[i_add + 1])
        else:
            summ -= int(additional_line[i_add + 1])

    return summ


def multiplication(mult_line):
    i_mult = 1
    # print('начало умножения', mult_line)

    while '*' in mult_line or '/' in mult_line:
        # print('в цикле', i_mult)
        if mult_line[i_mult] == '*':
            mult = int(mult_line[i_mult - 1]) * int(mult_line[i_mult + 1])
            del mult_line[i_mult - 1]
            del mult_line[i_mult - 1]
            del mult_line[i_mult - 1]
            mult_line.insert(i_mult - 1, mult)
            # print('в умножении после действия', mult_line)
        elif mult_line[i_mult] == '/':
            mult = int(mult_line[i_mult - 1]) / int(mult_line[i_mult + 1])
            # print(mult)
            del mult_line[i_mult - 1]
            del mult_line[i_mult - 1]
            del mult_line[i_mult - 1]
            mult_line.insert(i_mult - 1, mult)
            # print('в делении после действия', mult_line)
        else:
            i_mult += 2
    add_result = addition(mult_line)
    # print(add_result)
    return add_result


def line_preparation(line):
    word = ''
    for char in line:
        if char.isdigit():
            word += str(char)
        elif char in actions:
            if word != '':
                splited_line.append(word)
            splited_line.append(char)
            word = ''
    if word != '':
        splited_line.append(word)


def bracket(splited_line):
    while '(' in splited_line and ')' in splited_line:
        # print('начало цикла со скобками')
        result_place = splited_line.index('(')
        temp_line = splited_line[splited_line.index('(') + 1:splited_line.index(')')]
        for i in range(splited_line.index(')'), splited_line.index('(') - 1, -1):
            del splited_line[i]
        # print('содержимое скобок', temp_line)
        temp_result = multiplication(temp_line)
        splited_line.insert(result_place, temp_result)
        # print('результат вычисления скобок', splited_line)

    else:
        # print('Скобок больше нет, вызываю умножение и деление')
        result = multiplication(splited_line)
    return result


temp_line = []
splited_line = []
actions = '+-*/()'
line_preparation(line)
# print(splited_line)
result_all = bracket(splited_line)
print('результат', result_all)

# зачёт! 🚀
