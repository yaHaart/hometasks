string = input('Введите строку: ')
word_list = string.split()
new_string = ''
for word in word_list:
    if word[0].islower():
        word = word.capitalize()
    new_string += word + ' '
print(new_string)
