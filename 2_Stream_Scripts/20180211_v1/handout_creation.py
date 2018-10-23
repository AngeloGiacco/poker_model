'''handout creation'''

# pylint: disable=E1601, C0301

import deuces
import random
import hand_evaluation

def handout(players_number):
    '''function to create all the hands, board, etc.'''

    if players_number < 2 or players_number > 10:
        print('Nr of players is greater than 1 and less than 11. Try again.')

    else:
        pass

    deck = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS',\
            '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AD',\
            '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC',\
            '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AH']
    board = []

    flop1 = deck[random.randint(0, len(deck) - 1)]
    board.append(['flop1', flop1])
    deck.remove(flop1)

    flop2 = deck[random.randint(0, len(deck) - 1)]
    board.append(['flop2', flop2])
    deck.remove(flop2)

    flop3 = deck[random.randint(0, len(deck) - 1)]
    board.append(['flop3', flop3])
    deck.remove(flop3)

    turn = deck[random.randint(0, len(deck) - 1)]
    board.append(['turn', turn])
    deck.remove(turn)

    river = deck[random.randint(0, len(deck) - 1)]
    board.append(['river', river])
    deck.remove(river)

    hands = []
    for i in range(players_number):

        globals()['hand_player%s' % i] = ['player' + str(i + 1)]
        for j in range(2):

            globals()['card%s' % j] = deck[random.randint(0, len(deck) - 1)]
            globals()['hand_player%s' % i].append(globals()['card%s' % j])
            deck.remove(globals()['card%s' % j])

        hands.append(globals()['hand_player%s' % i])

    best5 = []
    for i in range(players_number):

        seven_cards = [flop1, flop2, flop3, turn, river]
        seven_cards.append(globals()['hand_player%s' % i][1])
        seven_cards.append(globals()['hand_player%s' % i][2])
        sc = ' '.join(seven_cards)
        globals()['best5_player%s' % i] = hand_evaluation.test_best_hand(sc)
        globals()['best5_player%s' % i].insert(0, 'player' + str(i + 1))
        best5.append(globals()['best5_player%s' % i])

    evaluator = deuces.Evaluator()

    for i in range(players_number):

        work_list = best5[i][-5:]
        wl1 = [\
        deuces.Card.new(work_list[0].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')), \
        deuces.Card.new(work_list[1].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c'))\
        ]
        wl2 = [\
        deuces.Card.new(work_list[2].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')), \
        deuces.Card.new(work_list[3].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')), \
        deuces.Card.new(work_list[4].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c'))\
        ]
        best5[i].append(evaluator.evaluate(wl2, wl1))

    return deck, board, hands, best5

# h = handout(6)
# print(h)
