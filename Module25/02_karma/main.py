import random


class UserErrors(Exception):
    def __str__(self):
        return 'Общая пользовательская ошибка'


class KillError(UserErrors):
    def __str__(self):
        return 'Убил живое существо'


class DrunkError(UserErrors):
    def __str__(self):
        return 'Выпил алкоголь'


class CarCrashError(UserErrors):
    def __str__(self):
        return 'Наехал на кого-то'


class GluttonyError(UserErrors):
    def __str__(self):
        return 'Грех обжорства'


class DepressionError(UserErrors):
    def __str__(self):
        return 'Грех уныния'


class Monk:
    __karma = 0

    def __init__(self):
        self.__karma = 0

    def set_karma(self, rand_karma):
        self.__karma += rand_karma

    def get_karma(self):
        # print('Сегодня карма', self.__karma)
        return self.__karma

    def one_day(self):
        if random.randint(8, 10) == 10:
            raise random.choice(UserErrors.__subclasses__())
        else:
            self.set_karma(random.randint(1, 7))


with open('errors.log', 'w') as file:
    pass

monk = Monk()
day = 0
while int(monk.get_karma()) < 500:
    day += 1
    try:
        monk.one_day()
        monk.get_karma()
    except Exception as ex:
        with open('errors.log', 'a') as file:
            file.write('день номер ' + str(day) + '     ' + ex.__str__() + '\n')

print(f'Просветление достигнуто за {day} дней')

# зачёт! 🚀
