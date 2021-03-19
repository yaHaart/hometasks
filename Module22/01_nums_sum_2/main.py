with open('numbers.txt', 'r', encoding='utf-8') as file:
    summ = 0
    for line in file:
        summ += int(line.replace(' ', ''))
with open('answers.txt', 'w', encoding='utf-8') as file_to_write:
    file_to_write.write(str(summ))
