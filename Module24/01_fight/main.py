import random


class Warrior:
    health = 100


left_warrior = Warrior()
right_warrior = Warrior()

while left_warrior.health > 0 and right_warrior.health > 0:
    random_punch = random.choice(['left_warrior', 'right_warrior'])
    if random_punch == 'left_warrior':
        right_warrior.health -= 20
        print(f'удар нанес левый боец. Здоровье {left_warrior.health} на {right_warrior.health} ')
    else:
        left_warrior.health -= 20
        print(f'удар нанес правый боец. Здоровье {left_warrior.health} на {right_warrior.health} ')

if left_warrior.health == 0:
    print('Победил правый боец')
else:
    print('Победил левый боец')
