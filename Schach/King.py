from Chess import *
class Chess_Piece_King(Chess_Piece):
    def __init__(self,name:str,x:int,y:int,size:int,costume:str,color:str,direction:int,player:str,status:bool,selected_by_player:bool):
        super().__init__(name,x,y,size,costume,color,direction,player,status,selected_by_player)

    def get_allowed_positions(self):
        print("{} has a current pos ({},{})".format(self.name,self.x,self.y))
        result = []

        #move like a tower just wit
        result.append([self.x + 1,self.y + 1])
        result.append([self.x - 1,self.y - 1])
        result.append([self.x + 1,self.y - 1])
        result.append([self.x - 1,self.y + 1])

        #------------------------------------move like a bishop----------------------:
        result.append([self.x - 1,self.y])
        result.append([self.x + 1,self.y])
        result.append([self.x,self.y + 1])
        result.append([self.x,self.y - 1])





        result = filter(myFuncForChessPiece,result)

        return result
