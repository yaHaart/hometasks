# some_iterables = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g'}
some_iterables = 'abcdefghijklmnop'
# some_iterables =  (0, 1, 2, 3, 4, 6, 5, 7, 8, 9, 10, 11, 12)


def crypto_function(iterable_object):
    return [some_iterables[i] for i in range(2, len(iterable_object)) if is_prime(i)]


def is_prime(n):
    divisor = 2
    while n % divisor != 0:
        divisor += 1
    return divisor == n


prime_list = crypto_function(some_iterables)
print(prime_list)
