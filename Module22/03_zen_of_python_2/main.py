import string as st  # TODO так как string - это название встроенной в питон библиотеки,
# TODO то для наименования переменных имя string - не самый лучший выбор
temp_list = []
letters = {}


def words_and_letters_count(string):
    # service_symbol = '!.*-\','
    service_symbol = st.punctuation  # TODO попробуйте воспользоваться таким приёмом
    number_of_words = len(string.split())
    for char in string:
        if char in service_symbol:
            pass
        elif char.lower() in letters:
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
inv_letters_dict = {value: key for key, value in letters.items()}
print(inv_letters_dict[min(letters.values())], min(letters.values()))

# TODO пока всё равно считает, что слов 137, а не 136
