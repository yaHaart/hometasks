from random import randint

with open('numbers.txt', 'w', encoding='UTF-8') as file:
    pass
summ = 0
while summ < 777:
    try:
        number = int(input('Введите целое число '))
        with open('numbers.txt', 'a', encoding='UTF-8') as file:
            file.write(str(number) + '\n')
        summ += number
        roulette = randint(1, 13)
        print(roulette)
        if roulette == 13:
            # TODO случайное исключение получить можно таким способом: random.choice(Exception.__subclasses__())
            raise BaseException()

    except ValueError:
        print('ввведите только число!')
    except BaseException:
        print('тебе не повезло')
        break
