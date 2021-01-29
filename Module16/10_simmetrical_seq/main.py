n = int(input('Кол-во чисел: '))
numbers = []
for _ in range(n):
    number = int(input('Число: '))
    numbers.append(number)

revers_numbers = numbers.copy()
revers_numbers.reverse()
flag = True

for i in range(len(numbers)):
    length_revers = len(revers_numbers)
    counter = 0
    for j in range(length_revers):
        if revers_numbers[-1 - j] != numbers[-1 - j]:
            flag = False
            break
        else:
            counter += 1

        if counter == length_revers:
            flag = True
    if flag:
        print('ПОследовательность ', numbers)
        print('Нужно приписать чисел ', len(numbers) - counter)
        print('Сами числа', end=' ')
        for ind in range(len(numbers) - counter - 1, -1, -1):
            print(numbers[ind], end=' ')
        break
    del revers_numbers[-1]
