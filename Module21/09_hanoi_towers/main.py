
def move(n, start, finish):
    if n == 1:
        print(f'переносим 1 диск со стержня № {start} на стержень № {finish}')
    else:
        tmp = 6 - start - finish
        move(n - 1, start, tmp)
        print(f'переносим {n} диск со стержня № {start} на стержень № {finish}')
        move(n - 1, tmp, finish)


number_of_disks = int(input('КОличество дисков: '))

move(number_of_disks, 1, 3)
