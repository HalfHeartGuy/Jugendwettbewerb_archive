from Bishop import berechne_between_positions_bishop
from Chess import  Chess_Piece, myFuncForChessPiece
from Tower import calc_between_position_tower

class Chess_Piece_Queen(Chess_Piece):
    def __init__(self,name:str,x:int,y:int,size:int,costume:str,color:str,direction:int,player:str,status:bool,selected_by_player:bool):
        super().__init__(name,x,y,size,costume,color,direction,player,status,selected_by_player)

    def get_allowed_positions(self):
        print("{} has a current pos ({},{})".format(self.name,self.x,self.y))

        result = []
        # move like a tower:
        for i in range(1,9):
            result.append([self.x - i,self.y])
            result.append([self.x + i,self.y])
            result.append([self.x,self.y + i])
            result.append([self.x,self.y - i])
        # move like a bishop
        for i in range(1,9):
            result.append([self.x + i, self.y + i])
            result.append([self.x - i, self.y + i])
            result.append([self.x + i, self.y - i])
            result.append([self.x - i, self.y - i])

        result = filter(myFuncForChessPiece,result)
        return result
    def moveTo(self, target_x: int, target_y: int, chess_boar: list):
        print("jetzt gilt eigene Regeln von Königin.")
        counter = 0
        ## jetzige Position ist (self.x, self.y), target ist (target_x, target_y)
        zwischen_zellen_index = []
        if (abs(target_x - self.x) == abs(target_y - self.y)) and abs(target_x - self.x) > 0:
            zwischen_zellen_index = berechne_between_positions_bishop(self.x,self.y,target_x,target_y)#wenn Queen wie ein Bishop läuft.
        elif self.x == target_x or self.y == target_y:
            zwischen_zellen_index = calc_between_position_tower(self.x,self.y,target_x,target_y)#Wenn Queen wie tower läuft





        print(str(zwischen_zellen_index))
        super().moveTo(target_x, target_y, chess_boar)











