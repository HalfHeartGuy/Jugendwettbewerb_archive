from Chess import Chess_Piece,myFuncForChessPiece

class Chess_Piece_Pawn(Chess_Piece):
    def __init__(self,name:str,x:int,y:int,size:int,costume:str,color:str,direction:int,player:str,status:bool,selected_by_player:bool):
        super().__init__(name,x,y,size,costume,color,direction,player,status,selected_by_player)

    def get_allowed_positions(self):
        print("{} {} has a current pos ({},{})".format(self.color,self.name,self.x,self.y))
        result = []
        if self.color == "white":
            result.append([self.x, self.y + 1])
            result.append([self.x + 1,self.y + 1])
            result.append([self.x - 1,self.y + 1])
            if self.y == 2:
                result.append([self.x, self.y + 2])
        if self.color == "black":
            result.append([self.x, self.y - 1])
            result.append([self.x + 1,self.y - 1])
            result.append([self.x - 1,self.y - 1])
            if self.y == 7:
                result.append([self.x, self.y - 2])



        result = filter(myFuncForChessPiece,result)


        resultforreturn = []


        for oneitem in result:

            resultforreturn.append(oneitem)




        return resultforreturn