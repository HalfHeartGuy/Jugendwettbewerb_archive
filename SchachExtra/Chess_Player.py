from Chess import *


class Chess_Player():
    def __init__(self, name:str, color: str):
        self.name = name
        self.color = color
        self.chess_board = []#zwei-dimensionale Liste

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color


    def select_one_chess_piece(self, one_chess_piece : Chess_Piece):
        one_chess_piece.selected_by_player()

    def move_one_chess_piece(self, one_chess_piece : Chess_Piece, target_x: int, target_y: int):
        if target_x < 8 and target_x > -1 and target_y < 8 and target_y > -1:

            old_x = one_chess_piece.x
            old_y = one_chess_piece.y

            self.chess_board[old_y][old_x] = None

            one_chess_piece.moveTo(target_x, target_y)
            one_chess_piece.unselect()

            self.chess_board[target_y][target_x] = one_chess_piece

        else:
            print(one_chess_piece.name + " konnte nicht zur " + str(target_x) + "," + str(target_y) + " bewegt werden.")



    def __str__(self):
        return "{} Player {}".format(self.color, self.name)

    def asign_to_game(self, chess_board: list):
        self.chess_board = chess_board