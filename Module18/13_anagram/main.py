word1 = input('Введите первое слово: ')
word2 = input('Введите второе слово: ')
dict_word1 = {}
dict_word2 = {}
for char in word1:
    if char in dict_word1.keys():
        dict_word1[char] = dict_word1[char] + 1
    else:
        dict_word1[char] = 1

for char in word2:
    if char in dict_word2.keys():
        dict_word2[char] = dict_word2[char] + 1
    else:
        dict_word2[char] = 1

if dict_word1 == dict_word2:
    print('Слова являются анаграммами друг друга')
else:
    print('Слова не являются анаграммами друг друга')

# зачёт! 🚀
