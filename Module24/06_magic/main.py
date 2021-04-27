
class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Fire):
            return Lightning()


class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()


class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()


class Storm:
    def __str__(self):
        return 'Шторм'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lightning:
    def __str__(self):
        return 'Молния'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Lava:
    def __str__(self):
        return 'Лава'


class Steam:
    def __str__(self):
        return 'Пар'


fire = Fire()
water = Water()

print(fire + water)

# зачёт! 🚀
