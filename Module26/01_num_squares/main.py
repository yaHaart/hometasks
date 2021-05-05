class SquareIterator:
    def __init__(self, limit: int) -> None:
        self.__limit = limit
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__limit:
            self.__counter += 1
            return self.__counter ** 2
        else:
            raise StopIteration


def square_iterator(limit: int):
    for ii in range(limit):
        yield (ii + 1) ** 2


iter1 = SquareIterator(10)
for i in iter1:
    print(i)

iter2 = square_iterator(limit=10)
for j in iter2:
    print('функция', j)

iter3 = (num ** 2 for num in range(1, 11))
for ij in iter3:
    print(ij)
