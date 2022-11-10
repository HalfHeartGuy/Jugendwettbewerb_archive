
from Chess_Player import *
from Tower import *
from Bishop import *
from King import *
from Knight import *
from Pawn_Richard import *
from Queen import *
class Chess_Game():
    def __init__(self, player1: Chess_Player, player2: Chess_Player):
        self.player1 = player1
        self.player2 = player2
        ###in this board we keep the information for each cell, with 2 dimentional list and value: chess_piece
        self.board = []

        self.chess_pieces = self.init_all_chess_pieces()


    def init_empty_row(self):
        result = []
        for i in range(0,9):
            result.append(None)
        return result




    def init_all_chess_pieces(self) -> dict:
        result = {}
        row1 = []
        row2 = self.init_empty_row()
        row3 = self.init_empty_row()
        row4 = self.init_empty_row()
        row5 = self.init_empty_row()
        row6 = self.init_empty_row()
        row8 = []
        row7 = []

        player1_tower_left_name = self.player1.get_color() + "_tower_left"
        player1_tower_left = Chess_Piece_Tower(name=player1_tower_left_name, x=1, y=1, size=2, costume="1", color=self.player1.get_color(), direction=90,
                                  player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_tower_left_name] = player1_tower_left
        row1.append(player1_tower_left)

        player1_knight_left_name = self.player1.get_color() + "_knight_left"
        player1_knight_left = Chess_Piece_Knight(name=player1_knight_left_name, x=2, y=1, size=2, costume="1",
                                               color=self.player1.get_color(), direction=90,
                                               player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_knight_left_name] = player1_knight_left
        row1.append(player1_knight_left)


        player1_bishop_left_name = self.player1.get_color() + "_bishop_left"
        player1_bishop_left = Chess_Piece_Bishop(name=player1_bishop_left_name, x=3, y=1, size=2, costume="1",
                                               color=self.player1.get_color(), direction=90,
                                               player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_bishop_left_name] = player1_bishop_left
        row1.append(player1_bishop_left)


        player1_queen_name = self.player1.get_color() + "_queen"
        player1_queen = Chess_Piece_Queen(name=player1_queen_name, x=4, y=1, size=2, costume="1",
                                               color=self.player1.get_color(), direction=90,
                                               player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_queen_name] = player1_queen
        row1.append(player1_queen)


        player1_king_name = self.player1.get_color() + "_king"
        player1_king = Chess_Piece_King(name=player1_king_name, x=5, y=1, size=2, costume="1",
                                               color=self.player1.get_color(), direction=90,
                                               player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_king_name] = player1_king
        row1.append(player1_king)


        player1_bishop_right_name = self.player1.get_color() + "_bishop_right"
        player1_bishop_right = Chess_Piece_Bishop(name=player1_bishop_right_name, x=6, y=1, size=2, costume="1",
                                               color=self.player1.get_color(), direction=90,
                                               player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_bishop_right_name] = player1_bishop_right
        row1.append(player1_bishop_right)


        player1_knight_right_name = self.player1.get_color() + "_knight_right"
        player1_knight_right = Chess_Piece_Knight(name=player1_knight_right_name, x=7, y=1, size=2, costume="1",
                                               color=self.player1.get_color(), direction=90,
                                               player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_knight_right_name] = player1_knight_right
        row1.append(player1_knight_right)



        player1_tower_right_name = self.player1.get_color() + "_tower_right"
        player1_tower_right = Chess_Piece_Tower (name=player1_tower_right_name, x=8, y=1, size=2, costume="1",
                                               color=self.player1.get_color(), direction=90,
                                               player=self.player1.get_name(), status=True, selected_by_player=False)
        result[player1_tower_right_name] = player1_tower_right
        row1.append(player1_tower_right)

        for i in range(1,9):
            player1_pawn_name = self.player1.get_color() + "_pawn_" + str(i)
            player1_pawn = Chess_Piece_Pawn(name=player1_pawn_name, x=i, y=2, size=2, costume="1",
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

        row8.append(player2_tower_left)

        player2_knight_left_name = self.player2.get_color() + "_knight_left"
        player2_knight_left = Chess_Piece_Knight(name=player1_knight_left_name, x=2, y=8, size=2, costume="1",
                                                color=self.player2.get_color(), direction=90,
                                                player=self.player2.get_name(), status=True, selected_by_player=False)
        result[player2_knight_left_name] = player2_knight_left

        row8.append(player2_knight_left)

        player2_bishop_left_name = self.player2.get_color() + "_bishop_left"
        player2_bishop_left = Chess_Piece_Bishop(name=player2_bishop_left_name, x=3, y=8, size=2, costume="1",
                                                color=self.player2.get_color(), direction=90,
                                                player=self.player2.get_name(), status=True, selected_by_player=False)
        result[player2_bishop_left_name] = player2_bishop_left

        row8.append(player2_bishop_left)

        player2_queen_name = self.player2.get_color() + "_queen"
        player2_queen = Chess_Piece_Queen(name=player2_queen_name, x=4, y=8, size=2, costume="1",
                                                 color=self.player2.get_color(), direction=90,
                                                 player=self.player2.get_name(), status=True, selected_by_player=False)
        result[player2_queen_name] = player2_queen

        row8.append(player2_queen)

        player2_king_name = self.player2.get_color() + "_king"
        player2_king = Chess_Piece_King(name=player2_king_name, x=5, y=8, size=2, costume="1",
                                               color=self.player2.get_color(), direction=90,
                                               player=self.player2.get_name(), status=True, selected_by_player=False)
        result[player2_king_name] = player2_king

        row8.append(player2_king)

        player2_bishop_right_name = self.player2.get_color() + "_bishop_right"
        player2_bishop_right = Chess_Piece_Bishop(name=player2_bishop_right_name, x=6, y=8, size=2, costume="1",
                                        color=self.player2.get_color(), direction=90,
                                        player=self.player2.get_name(), status=True, selected_by_player=False)
        result[player2_bishop_right_name] =player2_bishop_right

        row8.append(player2_bishop_right)

        player2_knight_right_name = self.player2.get_color() + "_knight_right"
        player2_knight_right = Chess_Piece_Knight(name=player2_knight_right_name, x=7, y=8, size=2, costume="1",
                                                color=self.player2.get_color(), direction=90,
                                                player=self.player2.get_name(), status=True, selected_by_player=False)
        result[player2_knight_right_name] = player2_knight_right

        row8.append(player2_knight_right)

        player2_tower_right_name = self.player2.get_color() + "_tower_right"
        player2_tower_right = Chess_Piece_Tower(name=player2_tower_right_name, x=8, y=8, size=2, costume="1",
                                                  color=self.player2.get_color(), direction=90,
                                                  player=self.player2.get_name(), status=True, selected_by_player=False)
        result[player2_tower_right_name] = player2_tower_right

        row8.append(player2_tower_right)

        for i in range(1,9):
            player2_pawn_name = self.player2.get_color() + "_pawn_" + str(i)
            player2_pawn = Chess_Piece_Tower(name=player2_pawn_name, x=i, y=7, size=2, costume="1",
                                                    color=self.player2.get_color(), direction=90,
                                                    player=self.player2.get_name(), status=True,
                                                    selected_by_player=False)
            result[player2_pawn_name] = player2_pawn
            row7.append(player2_pawn)



        self.board.append(row1)
        self.board.append(row2)
        self.board.append(row3)
        self.board.append(row4)
        self.board.append(row5)
        self.board.append(row6)
        self.board.append(row7)
        self.board.append(row8)

        return result

    def check_piece_for_position(self, x, y) -> Chess_Piece:
        return self.board[y-1][x-1]
