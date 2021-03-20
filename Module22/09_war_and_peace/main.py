import zipfile

letters_dict = {}


def letter_count(string):
    for char in string:
        if char == ' ' or char == '\n':
            pass
        elif char in letters_dict:
            letters_dict[char] += 1
        else:
            letters_dict[char] = 1


with zipfile.ZipFile('voyna-i-mir.zip') as zf:
    zf.extractall()

with open('voyna-i-mir.txt', 'r', encoding='utf-8') as file:
    for line in file:
        letter_count(line)

print()
sorted_values = sorted(letters_dict.values(), key=None, reverse=True)
with open('result.txt', 'w', encoding='utf-8') as rf:
    pass

with open('result.txt', 'a', encoding='utf-8') as rf:
    for sorted_value in sorted_values:
        for key in letters_dict.keys():
            if sorted_value == letters_dict[key]:
                print(key, letters_dict[key])
                rf.write(str(key) + '  ' + str(letters_dict[key]) + '\n')
                letters_dict.pop(key)
                break
