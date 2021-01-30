line = 'qsdhrftsxcvhlmj'
new_list = line.split('h')
print(new_list)
revers_list = new_list[1][::-1]
print(revers_list)
new_line = new_list[0] + 'h' + revers_list + 'h' + new_list[2]
print(new_line)
