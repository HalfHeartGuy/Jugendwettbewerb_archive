
from Chess_Game import *
from Chess_Player import *

player1 = Chess_Player("Jiaen", "white")
player2 = Chess_Player("Jason", "black")
one_chess_game = Chess_Game(player1, player2)
print(one_chess_game.board)


#erster Zug von Player1 von der Queen

selected_chess_piece = one_chess_game.check_piece_for_position(2,0)
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,5,3)

#erster Zug von Player 2 von den Läufer
selected_chess_piece = one_chess_game.check_piece_for_position(3,7)
one_chess_game.player2.move_one_chess_piece(selected_chess_piece,0,4)






"""
selected_chess_piece = one_chess_game.check_piece_for_position(3,0)
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,2,0)
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,4,2)
"""
