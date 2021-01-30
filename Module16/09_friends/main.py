friend_number = int(input('Кол-во друзей: '))
receipt_number = int(input('Долговых расписок: '))
balance = {}
for i in range(1, friend_number + 1):
    balance[i] = 0

print(balance)
for i in range(1, receipt_number + 1):
    who = int(input('Кому: '))
    to_whom = int(input('От кого: '))
    summ = int(input('Сколько '))
    balance[who] += summ
    balance[to_whom] -= summ
    print()

print('Баланс друзей ')
for key, value in balance.items():
    print(key, ":", value)

# зачёт! 🚀
