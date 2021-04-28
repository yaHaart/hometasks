class Property:

    def __init__(self, worth=0):
        self.worth = worth

    def tax(self):
        pass


class Appartment(Property):
    def tax(self):
        print(f'Налог на квартиру стоимостью {self.worth} составляет {self.worth/1000}')


class Car(Property):
    def tax(self):
        print(f'Налог на машину стоимостью {self.worth} составляет {self.worth/200}')


class CountryHouse(Property):
    def tax(self):
        print(f'Налог на дом стоимостью {self.worth} составляет {self.worth/200}')


appart = Appartment(1000000)
appart.tax()

car = Car(500000)
car.tax()

house = CountryHouse(10000000)
house.tax()

appart2 = Appartment()
appart2.tax()
