''' poker test '''

# pylint: disable=E1101, E1601

import board
import deck
import hand
import player
import pot

deck = deck.Deck()
# print(deck.show_deck())
# print(deck.card43.show_card())
# print(deck.nth_card(23).show_card(), deck.nth_card(23).figure(), deck.nth_card(23).color(), deck.nth_card(23).value())
# print(deck.draw_by_number(1).show_card())
# print(deck.show_deck())
# print(deck.draw_by_name('AS').show_card())
# print(deck.show_deck())
# print(deck.make_board())
# print(deck.make_hand())
# print(len(deck.show_deck()))
# print(deck.show_deck())
# deck.nth_card(66).show_card()

board = board.Board(deck.make_board())
# print(deck.show_deck())
# print(board.show_board())
# print(board.flop())
# print(board.flop1().show_card())
# print(board.flop2().show_card())
# print(board.flop3().show_card())
# print(board.turn().show_card())
# print(board.river().show_card())

hand1 = hand.Hand(deck.make_hand())
# print(deck.show_deck())
# print(hand1.show_hand())
# print(hand1.show()[0].show_card())
# print(hand1.show()[0].value())
# print(hand1.best_five(board))
# print(hand1.hand_strength(board))

hand2 = hand.Hand(deck.make_hand())
# print(deck.show_deck())
# print(hand2.show_hand())
# print(hand2.show()[1].show_card())
# print(hand2.show()[1].value())
# print(hand2.best_five(board))
# print(hand2.hand_strength(board))

player1 = player.Player(1, 100)
player1.add_hand(hand1)
# print(player1.show_player_hand().show_hand()[0].show_card())
# print(player1.show_player_hand().show_hand()[0].color())
# print(player1.show_player_hand().hand_strength(board))
# player1.increase_chips(50)
# player1.add_position(4)

player2 = player.Player(2, 100)
player2.add_hand(hand2)
# print(player2.show_player_hand().show_hand()[1].show_card())
# print(player2.show_player_hand().show_hand()[1].color())
# print(player2.show_player_hand().hand_strength(board))
# player2.decrease_chips(30)
# player2.add_position(7)

pot = pot.Pot()
# print(pot.show_pot())
# pot.increase_pot(55)
# print(pot.show_pot())
# POT = pot.Pot()
# print(POT.show_pot())
# POT.increase_pot(24)
# print(POT.show_pot())
# POT.increase_pot(6)
# print(POT.show_pot())
