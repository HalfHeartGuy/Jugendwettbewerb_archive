
from Chess import  Chess_Piece, myFuncForChessPiece
class Chess_Piece_Bishop(Chess_Piece):
    def __init__(self,name:str,x:int,y:int,size:int,costume:str,color:str,direction:int,player:str,status:bool,selected_by_player:bool):
        super().__init__(name,x,y,size,costume,color,direction,player,status,selected_by_player)

    def get_allowed_positions(self):
        print("{} has a current pos ({},{})".format(self.name,self.x,self.y))

        result = []
        for i in range(1,9):
            result.append([self.x + i, self.y + i])
            result.append([self.x - i, self.y + i])
            result.append([self.x + i, self.y - i])
            result.append([self.x - i, self.y - i])

        result = filter(myFuncForChessPiece,result)

        return result









