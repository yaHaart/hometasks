import re

string = 'South 17, North 13, East 15, West 11'
opt = re.sub(r'[^\w\s]', '', string)
str_list = opt.split()
coordinates = {str_list[x]: int(str_list[x + 1]) for x in range(0, len(str_list), 2)}
print(coordinates)
oy = coordinates['North'] - coordinates['South']
ox = coordinates['East'] - coordinates['West']
print('Координаты: ', ox, oy)

# зачёт! 🚀
# очень круто получилось!
