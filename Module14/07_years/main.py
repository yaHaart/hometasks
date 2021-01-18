start = int(input('Введите начало промежутка '))
end = int(input('Введите конец промежутка '))

for i in range(start, end + 1):
    line = str(i)
    if line[1] == line[2] == line[3] or line[0] == line[2] == line[3] or line[0] == line[1] == line[3] or line[0] == \
            line[1] == line[2]:
        print(i)

# зачёт! 🚀
