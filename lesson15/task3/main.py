cell_list = [3, 0, 6, 2, 12, 3, 2, 6, 9, 7, 6, 55, 14, 16, 1]
bad_cells = []
print('Кол-во клеток: ', len(cell_list))
for i in range(len(cell_list)):
    print(f'Эффективность {i + 1} клетки: {cell_list[i]}')
    if i > cell_list[i]:
        bad_cells.append(cell_list[i])
print('Неподходящие значения: ', bad_cells)
