
from Chess_Game import *
from Chess_Player import *

player1 = Chess_Player("Jiaen", "white")
player2 = Chess_Player("Richard", "black")
one_chess_game = Chess_Game(player1, player2)






selected_chess_piece = one_chess_game.check_piece_for_position(2,2) #ich habe hier für den Bauer von Position 2,2 genommen.
one_chess_game.player1.move_one_chess_piece(selected_chess_piece,2,3)

#Nur test code mit Schach spielen NICHTS zu tun
print(one_chess_game.check_piece_for_position(2,2))