from random import randint, choice

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

        if roulette == 13:
            #  случайное исключение получить можно таким способом: random.choice(Exception.__subclasses__())
            raise choice(Exception.__subclasses__())

    except ValueError:
        print('ввведите только число!')
    except Exception as ex:
        print('тебе не повезло')
        print(ex.__doc__)  # это чтобы видеть, что происходит
        break
