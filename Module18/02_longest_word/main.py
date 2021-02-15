string = input('Введите строку: ')
words_list = string.split()
max_word = ''
count = 0
for word in words_list:
    if len(word) > count:
        max_word = word
        count = len(word)

print(f'Самое длинное слово "{max_word}" содержит {count} символов')

# зачёт! 🚀
