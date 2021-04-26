from random import randint


class Parent:
    def __init__(self, name, age, child_list):
        self.name = name
        self.age = age
        self.child_list = child_list

    def info(self):
        print('______________________')
        print(self.name, self.age)
        print('_________ДЕТИ_________')
        for child in self.child_list:
            print(child.name, child.age)
        print()


class Child:
    calm_dict = {
        0: 'Истерика',
        1: 'Плач',
        2: 'Беспокойство',
        3: 'Норма',
        4: 'Спокойствие',
        5: 'Умиротворение'
    }

    hunger_dict = {
        0: 'Жуткий голод',
        1: 'Голод',
        2: 'Сытость',
        3: 'Переел'
    }

    def __init__(self, name, age, calm=5, hunger=3):
        self.name = name
        self.age = age
        self.calm = calm
        self.hunger = hunger

        if calm not in self.calm_dict:
            raise BaseException('Спокойстивие бывает от 0 до 5, не больше и не меньше ')
        if hunger not in self.hunger_dict:
            raise BaseException('Голод бывает от 0 до 3')

    def child_get_hunger(self):
        if self.hunger > 0:
            self.hunger -= 1
            print('Дети проголодались')
        else:
            print('уровень голода превысил все допустимые значения')

    def child_has_meal(self):
        if self.hunger == 3:
            print('больше не могу есть')
        else:
            self.hunger += 1


son = Child('Николай', 6, hunger=2)
daughter = Child('Ольга', 10, hunger=2)
father = Parent('Анатолий', 36, [son, daughter])
mather = Parent('Наталья', 35, [son, daughter])

father.info()
mather.info()

days = 1
for _ in range(30):
    print('------ начался день', days, '------')
    son.child_get_hunger()
    daughter.child_get_hunger()

    choice = randint(0, 2)
    if choice > 0:
        son.child_has_meal()
        daughter.child_has_meal()
        print('Покормили детей ')

    days += 1
