letters_dict = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

with open('text.txt', 'r', encoding='UTF-8') as file:
    text = file.read()

for char in text:
    if char.lower() in letters_dict:
        letters_dict[char.lower()] += 1
    else:
        letters_dict[char.lower()] = 1

count = 0
summ = 0

for key, value in letters_dict.items():
    if key in alphabet:
        count += 1
        summ += value

share_letters ={}
for key, value in letters_dict.items():
    if key in alphabet:
        share_letters[key] = round(value / summ, 3)

sorted_values = sorted(share_letters.values(), key=None, reverse=True)


with open('analysis.txt', 'w', encoding='utf-8') as file:
    pass

with open('analysis.txt', 'a', encoding='utf-8') as file:
    for sorted_value in sorted_values:
        for key in share_letters.keys():
            if sorted_value == share_letters[key]:
                file.write(str(key) + '   ' + str(share_letters[key]) + '\n')
                del share_letters[key]
                break

# зачёт! 🚀
