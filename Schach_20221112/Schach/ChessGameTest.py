
from Chess_Game import *
from Chess_Player import *

player1 = Chess_Player("Jiaen", "white")
player2 = Chess_Player("Jason", "black")
one_chess_game = Chess_Game(player1, player2)
print(one_chess_game.board)


#erster Zug von Player1, move tower
selected_chess_piece = one_chess_game.check_piece_for_position(2,0)
one_chess_game.player1.move_one_chess_piece(selected_chess_piece, 7, 5)
selected_chess_piece = one_chess_game.check_piece_for_position(5,0)
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,1,4)




"""
selected_chess_piece = one_chess_game.check_piece_for_position(3,0)
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,2,0)
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,4,2)
"""