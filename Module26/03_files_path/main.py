import os


def gen_files_path(end, start='/'):
    with open('log.txt', 'a') as file:
        object_list = os.listdir(path=start)
        for i_object in object_list:
            if os.path.isfile(os.path.join(start, i_object)):
                file.write(os.path.join(start, i_object) + '\n')

            elif os.path.isdir(os.path.join(start, i_object)):
                if os.path.join(start, i_object) == end:
                    break
                gen_files_path('/', os.path.join(start, i_object))

            else:
                print('не знаю что', i_object)


start_catalog = '/Users/haart/PycharmProjects'
end_catalog = '/Users/haart/PycharmProjects/python_basic/Module26/03_files_path'
with open('log.txt', 'w') as f:
    pass

gen_files_path(end=end_catalog, start=start_catalog)
