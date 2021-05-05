list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

can_continue = True
res = (x * y for x in list_1 for y in list_2)
for i in res:
    print(i)
    if i == to_find:
        print('Found!!!')
        can_continue = False
        break
