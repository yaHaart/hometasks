temp_list = []
letters = {}


def words_and_letters_count(string):
    number_of_words = len(string.split())
    for char in string:
        if char.lower() in letters:
            letters[char.lower()] += 1
        elif char == ' ' or char == '\n':
            pass
        else:
            letters[char.lower()] = 1
    return number_of_words


line_count = 0
word_count = 0
letters_count = 0
with open('zen.txt', 'r', encoding='utf=8') as file:
    for line in file:
        line_count += 1
        word_count += words_and_letters_count(line)

for value in letters.values():
    letters_count += value
print(letters_count, word_count, line_count)
inv_letters_dict = {value: key for key, value in letters.items()}  # TODO Количество букв в файле: 652
# TODO вместо 137 должно быть 136 так как "--" словом не является
print(inv_letters_dict[max(letters.values())], max(letters.values()))  # TODO Реже всего встречается буква k (2 раза)
