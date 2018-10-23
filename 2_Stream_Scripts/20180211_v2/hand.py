''' hand class '''

# pylint: disable=E1601

import deuces
import best5

class Hand(object):
    ''' hand class '''
    
    def __init__(self, hand):
        ''' hand initialization '''
        
        self.__hand = hand
        self.__card1 = hand[0]
        self.__card2 = hand[1]

    def show_hand(self):
        ''' show hand '''

        return self.__hand

    def best_five(self, board):
        ''' best 5 out of 7 '''

        hand_and_board = self.__card1.show_card() + ' ' + self.__card2.show_card() + ' ' + \
        board.flop1().show_card() + ' ' + board.flop2().show_card() + ' ' + board.flop3().show_card() + ' ' + \
        board.turn().show_card() + ' ' + board.river().show_card()

        return best5.test_best_hand(hand_and_board)

    def hand_strength(self, board):
        ''' hand strength '''

        evaluator = deuces.Evaluator()
        b5 = self.best_five(board)

        h1 = b5[0].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        h2 = b5[1].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        b1 = b5[2].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        b2 = b5[3].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        b3 = b5[4].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        hl = [deuces.Card.new(h1), deuces.Card.new(h2)]
        bl = [deuces.Card.new(b1), deuces.Card.new(b2), deuces.Card.new(b3)]
        strength = evaluator.evaluate(bl, hl)

        return strength
