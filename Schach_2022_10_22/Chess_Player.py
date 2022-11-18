from Chess import *

class Chess_Player():
    def __init__(self, name:str, color: str):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color


    def select_one_chess_piece(self, one_chess_piece : Chess_Piece):
        one_chess_piece.selected_by_player()

    def move_one_chess_piece(self, one_chess_piece : Chess_Piece, target_x: int, target_y: int):
        one_chess_piece.moveTo(target_x,target_y)
        one_chess_piece.unselect()