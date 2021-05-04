from random import choice, randint


class Person:

    def __init__(self, name, surname, age):
        self.set_name(name)
        self.set_surname(surname)
        self.age(age)

    def set_name(self, name):
        self.__name = name
        return self.__name

    def set_surname(self, surname):
        self.__surname = surname
        return self.__surname

    def age(self, age):
        self.__age = age
        return self.__age


class Employee(Person):
    @staticmethod
    def salary():
        return 0


class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        # NOTE если метод полностью повторяет родительский, то переопределять его не нужно

    @staticmethod
    def salery():
        return 13000


class Agent(Employee):
    def __init__(self, name, surname, age, money):
        super().__init__(name, surname, age)
        self.money = money

    def salery(self):
        return 5000 + 0.05 * self.money


class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours

    def salery(self):
        return 100 * self.hours


random_names = [
    'Оля',
    'Маша',
    'Саша',
    'Ира',
    'Наташа',
    'Валя',
    'Лена',
    'Варвара',
    'Настя'
]

random_surnames = [
    'Иванова',
    'Петрова',
    'Кузнецова',
    'Кропотова',
    'Ленина',
    'Крупская',
    'Смирнова',
    'СИнепупенко',
    'Сидорова'
]

employee_list = []

for _ in range(3):
    employee_list.append(Manager(choice(random_names), choice(random_surnames), randint(18, 65)))
    employee_list.append(Agent(choice(random_names), choice(random_surnames), randint(18, 65), randint(50000, 500000)))
    employee_list.append(Worker(choice(random_names), choice(random_surnames), randint(18, 65), randint(20, 45)))
summ = 0
for i_employee in employee_list:
    summ += i_employee.salery()

print('ФОТ ', summ)

# зачёт! 🚀
