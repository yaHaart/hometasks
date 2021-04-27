import math


class Circle:
    def __init__(self, center=[0, 0], radius=1):
        self.center = center
        self.radius = radius

    def square(self):
        print('Площадь искомого круга ', self.radius ** 2 * math.pi)

    def perimeter(self):
        print('Периметр искомого круга ', 2 * math.pi * self.radius)

    def multiply(self, k=1):
        self.radius *= k
        print('Радиус окружности увеличился в', k, 'раз и составил', self.radius)

    def cross(self, other_center, other_radius):
        distance = math.sqrt((other_center[0] - self.center[0]) ** 2 + (other_center[1] - self.center[1]) ** 2)
        if other_center == self.center:
            print('Центры окружностей совпадают.')
        elif distance > other_radius + self.radius:
            print('Окружности не пересекаются ')
        else:
            print('Окружности пересекаются')


circle_1 = Circle([1, 2], 3)
circle_1.square()
circle_1.perimeter()
circle_1.multiply(2)
circle_2 = Circle([1, 2], 2)
circle_1.cross(circle_2.center, circle_2.radius)

# зачёт! 🚀
