from random import randint, choice


class Students:
    def __init__(self, name, surname, group, grades, avg_grade=0):
        self.name = name
        self.surname = surname
        self.group = group
        self.grades = grades
        self.avg_grade = avg_grade


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

students_group = list()
for _ in range(10):
    students_group.append(Students(choice(random_names), choice(random_surnames),
                                   'группа ' + str(randint(1, 5)), [randint(1, 5) for i in range(5)]))

print('Вся группа')
avg_list = list()
for student in students_group:
    student.avg_grade = sum(student.grades) / len(student.grades)
    avg_list.append(student.avg_grade)
    print(student.name, student.surname, student.group, '     средний балл: ', student.avg_grade)
sorted_list = sorted(avg_list)

print()
print('отсортированная группа')
for i in sorted_list:
    for student in students_group:
        if student.avg_grade == i:
            print(student.name, student.surname, student.group, '     средний балл: ', student.avg_grade)
            students_group.pop(students_group.index(student))
            break
