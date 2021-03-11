index_number = 17


def fibonachi(number, next_number, count):

    if count < index_number:
        count += 1
        fibonachi(next_number, next_number + number, count)
    else:
        print(index_number, '-ый член ряда Фибоначчи', number)


fibonachi(1, 1, 1)
