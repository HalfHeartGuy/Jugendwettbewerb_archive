
from Chess_Game import *
from Chess_Player import *

player1 = Chess_Player("Jiaen", "white")
player2 = Chess_Player("Jason", "black")
one_chess_game = Chess_Game(player1, player2)
print(one_chess_game.board)


#erster Zug von Player1 von der Queen

selected_chess_piece = one_chess_game.check_piece_for_position(3,0)
#oben rechts
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,7,4)
#links
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,0,4)
#rechts
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,6,4)
#unten
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,6,0)
#oben
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,6,3)
#unten links
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,3,0)
#oben
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,3,7)
#unten rechts
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,5,5)
#oben links
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,3,7)








"""
selected_chess_piece = one_chess_game.check_piece_for_position(3,0)
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,2,0)
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,4,2)
"""
