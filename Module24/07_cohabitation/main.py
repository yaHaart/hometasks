from random import randint


class Man:
    def __init__(self, name, hungry=50):
        self.name = name
        self.hungry = hungry

    def eat(self):
        self.hungry += 1

    def work(self):
        self.hungry -= 1

    def play(self):
        self.hungry -= 1

    def get_hungry(self):
        self.hungry -= 1


class Fridge:
    def __init__(self, frost_food=50):
        self.frost_food = frost_food

    def eat(self):
        if self.frost_food >0:
            self.frost_food -= 1
            return self.frost_food
        else:
            return 0

    def shopping(self):
        self.frost_food += 1


class Locker:
    def __init__(self, locker_money=0):
        self.locker_money = locker_money

    def shopping(self):
        if self.locker_money > 10:
            self.locker_money -= 10
            return self.locker_money
        else:
            return 0

    def work(self):
        self.locker_money += 1


man_1 = Man('Ваня')
man_2 = Man('Маня')
fridge = Fridge()
locker = Locker()

for i in range(365):
    dice = randint(1, 6)
    if man_1.hungry < 20:
        if fridge.eat():
            man_1.eat()
        else:
            man_1.get_hungry()

    elif fridge.frost_food < 10:
        if locker.shopping():
            fridge.shopping()
        else:
            man_1.get_hungry()

    elif locker.locker_money < 50:
        man_1.work()
        locker.work()
    elif dice == 1:
        man_1.work()
        locker.work()
    elif dice == 2:
        if fridge.eat():
            man_1.eat()
        else:
            man_1.get_hungry()
    else:
        man_1.play()

    dice = randint(1, 6)
    if man_2.hungry < 20:
        if fridge.eat():
            man_2.eat()
        else:
            man_2.get_hungry()

    elif fridge.frost_food < 10:
        if locker.shopping():
            fridge.shopping()
        else:
            man_2.get_hungry()

    elif locker.locker_money < 50:
        man_2.work()
        locker.work()
    elif dice == 1:
        man_2.work()
        locker.work()
    elif dice == 2:
        if fridge.eat():
            man_2.eat()
        else:
            man_2.get_hungry()
    else:
        man_1.play()

    if man_1.hungry <= 0:
        print(man_1.name, ' умер')
        break
    if man_2.hungry <= 0:
        print(man_1.name, ' умер')
        break
    print(f'Прошел {i} день.  {man_1.name} имеет сытость {man_1.hungry}. '
          f'{man_2.name} имеет сытость {man_2.hungry}.  Еды {fridge.frost_food}, денег {locker.locker_money}')
