number_countries = int(input('Кол-во стран: '))
countries_dict = dict()
for i_country in range(number_countries):
    user_input = input(f'{i_country + 1} страна: ')
    user_dict = user_input.split()
    if countries_dict == {}:
        countries_dict = {user_dict[0]: [user_dict[i] for i in range(1, 4)]}
    else:
        countries_dict.update({user_dict[0]: [user_dict[i] for i in range(1, 4)]})


number_cities = 3
city_print = ''
countries_print = ''
for i_cities in range(number_cities):
    user_city = input('Город ')
    for key in countries_dict:
        if user_city in countries_dict[key]:
            city_print = user_city
            countries_print = key
            break

    if city_print != '' and countries_print != '':
        print(f'Город {city_print} расположен в стране {countries_print}.')
    else:
        print(f'По городу {user_city} данных нет.')
    city_print = ''
    countries_print = ''
