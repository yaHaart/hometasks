from random import randint

max_number = randint(10, 15)
number_to_guess = randint(0, max_number)
print('Загадано число от 0 до', max_number, 'это число ', number_to_guess)
number_list = [x for x in range(max_number + 1)]
print(number_list)
guess_list = []
guesses = 3


for i_guess in range(guesses):
    for _ in range(randint(3, 5)):
        guess_list.append(randint(0, max_number))
    print(f'{i_guess + 1} попытка ', guess_list)
    print(f'Нужное число есть среди вот этих чисел: {set(guess_list)}?')
    if number_to_guess in set(guess_list):
        print('Ответ Артема: да ', end='')
        number_list.clear()
        for i_number in set(guess_list):
            number_list.append(i_number)
    else:
        print('нет')
        for i_number in set(guess_list):
            if i_number in number_list:
                number_list.remove(i_number)
    guess_list.clear()
print('Артём мог загадать следующие числа: ', number_list)

# зачет!
