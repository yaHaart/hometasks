import os


def gen_files_path(start, count=0):
    with open('log.txt', 'a') as file:
        object_list = os.listdir(path=start)
        for i_object in object_list:
            if i_object[0] == '.':
                print('что-то начинается с точки', i_object)
                pass
            elif os.path.isfile(os.path.join(start, i_object)):
                if len(i_object.split('.')) > 1:
                    extention = i_object.split('.')[1]
                    if extention == 'py':
                        with open(os.path.join(start, i_object), 'r') as py_file:
                            for line in py_file:
                                if line != '\n':
                                    count +=1
                file.write(os.path.join(start, i_object) + '\n')

            elif os.path.isdir(os.path.join(start, i_object)):
                count += gen_files_path(os.path.join(start, i_object), count)

            else:
                print('не знаю что', i_object)

    return count


start_catalog = '/Users/haart/PycharmProjects/python_basic/Module25/'
with open('log.txt', 'w') as f:
    pass

count = 0
print(gen_files_path(start=start_catalog))
