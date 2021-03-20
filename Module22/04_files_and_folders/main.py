import os


def go_in_folder(path_to_go, file_count, file_size):
    for i_elem in os.listdir(path_to_go):
        if os.path.isfile(os.path.join(path_to_go, i_elem)):
            file_count += 1
            file_size += os.path.getsize(os.path.join(path_to_go, i_elem))

        elif os.path.isdir(os.path.join(path_to_go, i_elem)):
            file_count, file_size = go_in_folder(os.path.join(path_to_go, i_elem), file_count, file_size)
    return file_count, file_size


path_to_folder = '/Users/haart/PycharmProjects/python_basic/'
summ, size = go_in_folder(path_to_folder, 0, 0)

print('Количество файлов:', summ, '       Размер, байт:', size)
