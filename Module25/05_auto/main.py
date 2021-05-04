import math


class Car:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.set_direction(direction)

    def set_direction(self, direction):
        if 0 <= direction <= 360:
            self.direction = math.radians(direction)
            return self.direction
        else:
            raise ValueError('направление в градусах от 0 до 360')

    def move(self, distance):
        self.x = self.x + distance * math.cos(self.direction)
        self.y = self.y + distance * math.sin(self.direction)


class Bus(Car):

    def __init__(self, x, y, direction, money=0, passangers=0):
        super().__init__(x, y, direction)
        self.passangers = passangers
        self.__money = money

    def passangers_in(self, passangers):
        self.passangers += passangers
        self.money_pay()

    def passangers_out(self, passangers):
        if self.passangers >= passangers:
            self.passangers -= passangers
        else:
            raise ValueError('пассажиры закончились')

    def money_pay(self):
        self.__money = self.passangers * self.direction
        print('сейчас денег', self.__money)


try:
    car = Car(0, 0, 90)
    car.move(10)
    car.set_direction(60)
    print(car.x, car.y)

    bus = Bus(0, 0, 90, 0, 0)
    bus.passangers_in(10)


except ValueError as ve:
    print(ve)

# зачёт! 🚀
