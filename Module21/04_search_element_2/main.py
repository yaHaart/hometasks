site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}
key_to_find = 'div'


def parsing_dict(struct, key_to_find):
    if key_to_find in struct:
        return struct[key_to_find]

    for value in struct.values():
        if isinstance(value, dict):
            result = parsing_dict(value, key_to_find)
            if result:
                break
    else:
        result = None
    return result


print(parsing_dict(site, key_to_find))
