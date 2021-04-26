import random

deck_on_hands = []
cards_suit = ['крести', 'пики', 'черви', 'буби']
croupier_cards = []
player_cards = []
winner = ''


class RandomCard:
    def __init__(self):
        while True:
            self.suit = random.choices(cards_suit)
            self.seniority = random.randint(1, 13)
            if self.seniority <= 10 and self.seniority != 1:
                self.card = str(self.seniority) + ' ' + self.suit[0]
            elif self.seniority == 1:
                self.card = 'Туз ' + self.suit[0]
            elif self.seniority == 11:
                self.card = 'Валет ' + self.suit[0]
            elif self.seniority == 12:
                self.card = 'Дама ' + self.suit[0]
            elif self.seniority == 13:
                self.card = 'Король ' + self.suit[0]

            if self.card not in deck_on_hands:
                deck_on_hands.append(self.card)
                break


def cards_count(list_of_cards):
    # print('начали считать карты')
    summ = 0
    for i_card in list_of_cards:
        # print(card.seniority)
        if i_card.seniority <= 10 and i_card.seniority != 1:
            # print('номинал', card.seniority)
            summ += i_card.seniority
        elif 10 < i_card.seniority <= 13:
            # print('картинка', card.seniority)
            summ += 10
        elif i_card.seniority == 1:
            # print('туз', card.seniority)
            summ += 11
        else:
            return 0
    # print(summ)
    if summ > 21:
        for i_card in list_of_cards:
            if i_card.seniority == 1:
                summ -= 10
    return summ


print('Начинаем сдачу.')

while len(croupier_cards) < 2:
    new_card = RandomCard()
    croupier_cards.append(new_card)

croupier_count = cards_count(croupier_cards)
print('На руках у крупье', croupier_cards[0].card, '  ', croupier_cards[1].card, '     что составляет', croupier_count)

while len(player_cards) < 2:
    new_card = RandomCard()
    player_cards.append(new_card)
player_count = cards_count(player_cards)
print('На руках у игрока', player_cards[0].card, '  ', player_cards[1].card, '     что составляет', player_count)

print('Добираем карты ')

while True:
    # print('вошли в цикл')
    while not 17 <= player_count and player_count <= 21:
        # print('запрос карты')
        new_card = RandomCard()
        # print(new_card.card)
        player_cards.append(new_card)
        player_count = cards_count(player_cards)
    print('НА руках у игрока ', end='')
    for card in player_cards:
        print(card.card, '  ', end='')
    print('     что составляет', player_count)

    if player_count > 21:
        winner = 'Крупье'
        # print(winner)
        break

    while not 17 <= croupier_count and croupier_count <= 21:
        new_card = RandomCard()
        croupier_cards.append(new_card)
        croupier_count = cards_count(croupier_cards)
    print('НА руках у крупье ', end='')
    for card in croupier_cards:
        print(card.card, '  ', end='')
    print('     что составляет', croupier_count)
    if croupier_count > 21:
        winner = 'Игрок'
    break

if winner != '':
    print('Победил',  winner)
elif croupier_count > player_count:
    print('ПОбеда крупье')
elif croupier_count == player_count:
    print('Ничья')
elif player_count > croupier_count:
    print('Победил игрок')
else:
    print('что-то пошло не так')
