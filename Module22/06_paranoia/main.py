alphabet_lowercase = 'abcdefghijklmnopqrstuvwxyz'
alphabet_capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = 0

with open('cipher_text.txt', 'w', encoding='utf-8') as temp:
    pass

with open('text.txt', 'r', encoding='UTF-8') as file:
    with open('cipher_text.txt', 'a', encoding='UTF-8') as rf:
        encrypted_line = ''
        for line in file:
            for char in line:
                if char.isupper():
                    encrypted_char = alphabet_capital[(alphabet_capital.index(char) + 1 + count) % 26]
                elif char.islower():
                    encrypted_char = alphabet_lowercase[(alphabet_lowercase.index(char) + 1 + count) % 26]
                else:
                    encrypted_char = char

                encrypted_line += encrypted_char
            count += 1

        rf.write(encrypted_line + '\n')


