
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
        row2 = []
        player1_tower_left_name = self.player1.get_color() + "_tower_left"
        player1_tower_left = Chess_Piece_Tower(name=player1_tower_left_name, x=1, y=1, size=2, costume="1", color=self.player1.get_color(), direction=90,
                                  player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_tower_left_name] = player1_tower_left
        row1.append(player1_tower_left)

        player1_knight_left_name = self.player1.get_color() + "_knight_left"
        player1_knight_left = Chess_Piece_Tower(name=player1_knight_left_name, x=2, y=1, size=2, costume="1",
                                               color=self.player1.get_color(), direction=90,
                                               player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_knight_left_name] = player1_knight_left
        row1.append(player1_knight_left)


        player1_bishop_left_name = self.player1.get_color() + "_bishop_left"
        player1_bishop_left = Chess_Piece_Tower(name=player1_bishop_left_name, x=3, y=1, size=2, costume="1",
                                               color=self.player1.get_color(), direction=90,
                                               player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_bishop_left_name] = player1_bishop_left
        row1.append(player1_bishop_left)


        player1_queen_name = self.player1.get_color() + "_queen"
        player1_queen = Chess_Piece_Tower(name=player1_queen_name, x=4, y=1, size=2, costume="1",
                                               color=self.player1.get_color(), direction=90,
                                               player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_queen_name] = player1_queen
        row1.append(player1_queen)


        player1_king_name = self.player1.get_color() + "_king"
        player1_king = Chess_Piece_Tower(name=player1_king_name, x=5, y=1, size=2, costume="1",
                                               color=self.player1.get_color(), direction=90,
                                               player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_king_name] = player1_king
        row1.append(player1_king)


        player1_bishop_right_name = self.player1.get_color() + "_bishop_right"
        player1_bishop_right = Chess_Piece_Tower(name=player1_bishop_right_name, x=6, y=1, size=2, costume="1",
                                               color=self.player1.get_color(), direction=90,
                                               player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_bishop_right_name] = player1_bishop_right
        row1.append(player1_bishop_right)


        player1_knight_right_name = self.player1.get_color() + "_knight_right"
        player1_knight_right = Chess_Piece_Tower(name=player1_knight_right_name, x=7, y=1, size=2, costume="1",
                                               color=self.player1.get_color(), direction=90,
                                               player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_knight_right_name] = player1_knight_right
        row1.append(player1_knight_right)



        player1_tower_right_name = self.player1.get_color() + "_tower_right"
        player1_tower_right = Chess_Piece_Tower(name=player1_tower_right_name, x=8, y=1, size=2, costume="1",
                                               color=self.player1.get_color(), direction=90,
                                               player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_tower_right_name] = player1_tower_right
        row1.append(player1_tower_right)

        for i in range(1,9):
            player1_pawn_name = self.player1.get_color() + "_pawn_" + str(i)
            player1_pawn = Chess_Piece_Tower(name=player1_pawn_name, x=i, y=2, size=2, costume="1",
                                                    color=self.player1.get_color(), direction=90,
                                                    player=self.player1.get_name(), status=True,
                                                    selected_by_player=False)
            result[player1_pawn_name] = player1_pawn
            row2.append(player1_pawn)



        player2_tower_left_name = self.player2.get_color() + "_tower_left"
        player2_tower_left = Chess_Piece_Tower(name=player2_tower_left_name, x=1, y=8, size=2, costume="1",
                                               color=self.player2.get_color(), direction=90,
                                               player=self.player2.get_name(), status=True, selected_by_player=False)
        result[player2_tower_left_name] = player2_tower_left

        row1.append(player2_tower_left)

        self.board.append(row1)
        self.board.append(row2)
        return result

    def check_piece_for_position(self, x, y) -> Chess_Piece:
        return self.board[y-1][x-1]
