print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
radius = float(input('Введите радиус: '))

if x * y <= radius:
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')

# зачёт! 🚀
