students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interests_and_age(students_dict):
    interests = []
    count = 0
    for i_student in students_dict:
        interests += (students_dict[i_student]['interests'])
        count += len(students_dict[i_student]['surname'])

    return interests, count


pairs = []
for i in students:
    print(i, students[i]['age'])
print()

list_of_interests, surnames = interests_and_age(students)
for interest in list_of_interests:
    print(interest)
print(surnames)
