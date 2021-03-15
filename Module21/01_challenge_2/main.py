max_number = 10


def print_next_number(number):
    if number <= max_number:
        print(number)
        print_next_number(number + 1)


print_next_number(1)

# зачет!
