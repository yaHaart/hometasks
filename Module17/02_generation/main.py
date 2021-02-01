n = int(input('введите число '))
numbers = [(1 if x % 2 == 0 else x % 5) for x in range(n)]
print(numbers)

# зачёт! 🚀
