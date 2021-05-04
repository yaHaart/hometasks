class Property:

    def __init__(self, worth=0):
        self.worth = worth

    def tax(self):
        pass


class Appartment(Property):
    def tax(self):
        print(f'Налог на квартиру стоимостью {self.worth} составляет {self.worth / 1000}')
        return self.worth / 1000


class Car(Property):
    def tax(self):
        print(f'Налог на машину стоимостью {self.worth} составляет {self.worth / 200}')
        return self.worth / 200


class CountryHouse(Property):
    def tax(self):
        print(f'Налог на дом стоимостью {self.worth} составляет {self.worth / 500}')
        return self.worth / 500


text_input = ''
summ = 0
while True:
    text_input = input('какое имущество у вас есть? введите в формате "что сколько стоит" ')
    if text_input == 'это все':
        break
    temp_list = text_input.split()
    try:
        if not temp_list[1].isdigit() and not int(temp_list[1]) > 0:
            raise AttributeError

        if temp_list[0].lower() == 'квартира':
            temp_property = Appartment(int(temp_list[1]))
            summ += temp_property.tax()
        elif temp_list[0].lower() == 'машина':
            temp_property = Car(int(temp_list[1]))
            summ += temp_property.tax()
        elif temp_list[0].lower() == 'дом':
            temp_property = CountryHouse(int(temp_list[1]))
            summ += temp_property.tax()
        else:
            print(' Неверный формат или неизвестная собственность. Только квартира машина или дом')

    except AttributeError:
        print('Проблема со стоимостью объекта')
    except IndexError:
        print('Проблема в формате. нужно примерно так: квартира 1000')
    except ValueError:
        print('стоимость должна быть целым натуральным числом')

money = int(input('Сколько денег у вас есть на налоги? '))

if money >= summ:
    print('У вас хватит денег на оплату налогов')
else:
    print(f'У вас не хватает {summ - money} рублей')

# зачёт! 🚀
