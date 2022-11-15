class Sprite():
    def __init__(self, name:str, x:int, y:int, size:int, costume:str, color:str, direction:int):
        self.name = name
        self.x = x
        self.y = y
        self.size = size
        self.costume = costume
        self.color = color
        self.direction = direction
    def moveTo(self,target_x,target_y):
        self.x = target_x
        self.y = target_y
##x,y:coordinate of current position
#size: wie groß ist meine Figur
#costume:der Dateiname meines Images
#color:color meines Images
#color:color meines Images
#direction:Richtung meiner Figur
#player:we, diese Figur gehört,sollte nur 2 geben.
#status:lebt oder getötet,wenn getötet heißt es nicht mehr bewegen darf.
#selected_by_player:nur ausgewählte Figur darf bewegen.



#Filter out Function for Chess Pieces.
def myFuncForChessPiece(result):
    return result[0] < 8 and result[0] > -1 and result[1] < 8 and result[1] > -1

class Chess_Piece(Sprite):
    def __init__(self,name:str,x:int,y:int,size:int,costume:str,color:str,direction:int,player:str,status:bool,selected_by_player:bool):
        super().__init__(name,x,y,size,costume,color,direction)
        self.player = player
        self.status = status
        self.selected_by_player = selected_by_player

    def moveTo(self,x,y,chess_board:list):
        if [x,y] in self.get_allowed_positions():
            print("Chess {} with current position ({},{}) is moved to ({},{})".format(self.name, self.x, self.y, x,y))
            self.x = x
            self.y = y
        else:
            print("Chess {} with current position ({},{}) can not be moved to ({},{})".format(self.name, self.x, self.y, x,y))

    #gibt an,welche positionen darf ein ausgewählte Figur im nächsten Schritt belegen.
    #Type dieser Funktion ist Liste von Tupeln,e.g. [(3,5),(4,4),...}
    def get_allowed_positions(self):
        pass
    def defeat(self,enemy_piece_name:str):
        pass

    def is_selected(self):
        self.selected_by_player = True

    def unselect(self):
        self.selected_by_player = False

    def __str__(self):
        return self.name
