my_tuple = ('a', 'c', 'v', 'c', 'd', 'v', 's', 'v')
char_to_count = 'v'
new_tuple = tuple()


def new_tuple_creating(number_chars):
    if number_chars == 0:
        new_tuple: tuple = ()
        return new_tuple
    elif number_chars == 1:
        new_tuple = my_tuple[my_tuple.index(char_to_count):]
        return new_tuple
    else:
        start = my_tuple.index(char_to_count)
        end = my_tuple.index(char_to_count, my_tuple.index(char_to_count) + 1)
        print(start, end)
        new_tuple = my_tuple[start:end + 1]
        return new_tuple


print('ответ', new_tuple_creating(my_tuple.count(char_to_count)))
