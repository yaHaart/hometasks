while True:
    ip_adress = input(' введите ip адрес ')
    ip_parts_list = ip_adress.split('.')
    print(ip_parts_list)
    parts_correct = 0
    flag = False
    if ip_adress.count('.') != 3:
        print("Адрес - это четыре числа, разделенные точками")
        break
    for part in ip_parts_list:
        if part.isdigit() and int(part) > 255:
            print(f'{part} превышает 255')
            flag = True
            break
        elif not part.isdigit():
            print(f'{part} - не целое число ')
            flag = True
            break
        else:
            parts_correct += 1
    if parts_correct == 4:
        print('IP-адрес корректен')
        break

    if flag:
        break