
from Chess_Player import *
from Tower import *
class Chess_Game():
    def __init__(self, player1: Chess_Player, player2: Chess_Player):
        self.player1 = player1
        self.player2 = player2
        ###in this board we keep the information for each cell, with 2 dimentional list and value: chess_piece
        self.board = []

        self.chess_pieces = self.init_all_chess_pieces()




    def init_all_chess_pieces(self) -> dict:
        result = {}
        row1 = []
        player1_tower_left_name = self.player1.get_color() + "_tower_left"
        player1_tower_left = Chess_Piece_Tower(name=player1_tower_left_name, x=1, y=1, size=2, costume="1", color=self.player1.get_color(), direction=90,
                                  player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_tower_left_name] = player1_tower_left
        row1.append(player1_tower_left)

        player2_tower_left_name = self.player2.get_color() + "_tower_left"
        player2_tower_left = Chess_Piece_Tower(name=player2_tower_left_name, x=1, y=8, size=2, costume="1",
                                               color=self.player2.get_color(), direction=90,
                                               player=self.player2.get_name(), status=True, selected_by_player=False)
        result[player2_tower_left_name] = player2_tower_left

        row1.append(player2_tower_left)

        self.board.append(row1)
        return result

    def check_piece_for_position(self, x, y) -> Chess_Piece:
        return self.board[x-1][y-1]