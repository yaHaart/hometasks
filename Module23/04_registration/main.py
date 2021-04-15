count = 0
with open('registrations_bad.log', 'w') as bad_file:
    pass
with open('registrations_good.log ', 'w', ) as good_file:
    pass

with open('registrations.txt', 'r') as base_file:
    for line in base_file:
        count += 1
        temp_list = line.split()

        try:
            if len(temp_list) < 3:
                raise IndexError
            if not temp_list[0].isalpha():
                raise NameError
            if '@' not in temp_list[1] or '.' not in temp_list[1]:
                raise SyntaxError
            if 10 >= int(temp_list[2]) or int(temp_list[2]) >= 99:
                raise ValueError
            with open('registrations_good.log ', 'a', encoding='UTF-8') as good_file:
                good_file.write(str(count) + '          ' + line)

        except IndexError:
            with open('registrations_bad.log', 'a') as bad_file:
                bad_file.write(str(count) + '   ' + 'IndexError    ' + line)
        except NameError:
            with open('registrations_bad.log', 'a') as bad_file:
                bad_file.write(str(count) + '   ' + 'NameError    ' + line)
        except SyntaxError:
            with open('registrations_bad.log', 'a') as bad_file:
                bad_file.write(str(count) + '   ' + 'SyntaxError    ' + line)
        except ValueError:
            with open('registrations_bad.log', 'a') as bad_file:
                bad_file.write(str(count) + '   ' + 'ValueError    ' + line)
