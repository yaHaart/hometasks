db = {
    ('Сидоров', 'Никита'): 35,
    ('сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Иванов', 'Иван'): 42
}

surname = 'Сидоров'

for human in db:
    if human[0].lower().find(surname.lower()) >= 0:
        print(human[0], human[1], db[human])

# зачет!
