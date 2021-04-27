class Potato:
    states = {0: 'Отсутсвует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.state]}')


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела\n')
            return False
        else:
            print('Вся картошка созрела. Можно собирать\n')
            return True


class Gardener:
    def __init__(self, name):
        self.name = name
        self.garden_bed = PotatoGarden(5)

    @staticmethod
    def care():
        print('Садовник ухаживает за грядкой')

    def harvesting(self):
        if self.garden_bed.are_all_ripe():
            print('Собрали всю картошку:', len(self.garden_bed.potatoes), 'кустов')
            self.garden_bed.potatoes = []

        else:
            print('Картошка еще не созрела')


gardener = Gardener('Иван')

for _ in range(3):
    gardener.care()
    gardener.garden_bed.grow_all()
    gardener.garden_bed.are_all_ripe()
gardener.harvesting()

print(gardener.garden_bed.potatoes)

# зачёт! 🚀
