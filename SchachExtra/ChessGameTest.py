
from Chess_Game import *
from Chess_Player import *

player1 = Chess_Player("Jiaen", "white")
player2 = Chess_Player("Richard", "black")
one_chess_game = Chess_Game(player1, player2)


print(one_chess_game.check_piece_for_position(1,2))
