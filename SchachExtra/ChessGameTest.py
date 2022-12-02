
from Chess_Game import *
from Chess_Player import *

player1 = Chess_Player("Jiaen", "white")
player2 = Chess_Player("Jason", "black")
one_chess_game = Chess_Game(player1, player2)


#print(one_chess_game.player1)

# ich habe hier für den ersten Schritt den Bauer von Position 1,1 genommen

#erster Zug von Player1
selected_chess_piece = one_chess_game.check_piece_for_position(3,0)
one_chess_game.player1.move_one_chess_piece(selected_chess_piece, 3, 5)
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,3,7)

"""
selected_chess_piece = one_chess_game.check_piece_for_position(1,0)
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,3,1)
print(one_chess_game.check_piece_for_position(1,0))

selected_chess_piece = one_chess_game.check_piece_for_position(2,0)
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,7,5)

#zweiter Zug von Player2
selected_chess_piece = one_chess_game.check_piece_for_position(0,6)
one_chess_game.player2.move_one_chess_piece(selected_chess_piece, 0, 4)
print(one_chess_game.check_piece_for_position(0,6))
selected_chess_piece = one_chess_game.check_piece_for_position(0,7)
one_chess_game.player2.move_one_chess_piece(selected_chess_piece, 0, 1)
print(one_chess_game.check_piece_for_position(0,7))

selected_chess_piece = one_chess_game.check_piece_for_position(4,7)
one_chess_game.player2.move_one_chess_piece(selected_chess_piece,4,6)
print(one_chess_game.check_piece_for_position(4,7))


selected_chess_piece = one_chess_game.check_piece_for_position(3,7)
one_chess_game.player2.move_one_chess_piece(selected_chess_piece,-1,7)
print(one_chess_game.check_piece_for_position(3,7))


# Nur test code mit Schach spielen NICHTS zu tun!!!
#print(one_chess_game.check_piece_for_position(1,1))
#print(one_chess_game.check_piece_for_position(1,2))
"""