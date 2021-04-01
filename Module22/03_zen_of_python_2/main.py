import string as st

temp_list = []
letters = {}


def words_and_letters_count(string_from_file):
    service_symbol = st.punctuation
    number_of_words = 0
    for word in string_from_file.split():
        for symbol in word:
            if symbol not in service_symbol:
                number_of_words += 1
                break

    for char in string_from_file:
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
