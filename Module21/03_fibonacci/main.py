index_number = 7
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(index_number, '-ый элемент ряда ', fibonacci(index_number))

# зачёт! 🚀
