from copy import deepcopy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def parsing_dict(struct, telephone_name):
    key1_to_find = 'title'
    key2_to_find = 'h2'
    title_to_change = 'Куплю/продам ' + telephone_name + ' недорого'
    h2_to_change = 'У нас самая низкая цена на ' + telephone_name
    if key1_to_find in struct:
        struct[key1_to_find] = title_to_change

    if key2_to_find in struct:
        struct[key2_to_find] = h2_to_change

    for value in struct.values():
        if isinstance(value, dict):
            result = parsing_dict(value, telephone_name)
            if result:
                break
    else:
        result = None

    return result


number_of_sites = 2

for _ in range(number_of_sites):
    telephone = input('Название телефона ')
    site_copy = deepcopy(site)
    parsing_dict(site_copy, telephone)
    print(site_copy)
    # print(site)
