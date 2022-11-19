
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
    def moveTo(self,target_x:int,target_y:int,chess_boar:list):
        print("jetzt gilt eigene Regeln von Läufer.")

        ## jetzige Position ist (self.x, self.y), target ist (target_x, target_y)
        zwischen_zellen_index = []

        if (target_y > self.y and self.x < target_x):
            zwischen_zellen_index.append([(self.x + i,self.y + i) for i in range(1,target_y - self.y)])
        elif (target_y < self.y and self.x > target_x):
            zwischen_zellen_index.append([(self.x - i,self.y - i) for i in range(1,self.y - target_y)])


        elif (target_y > self.y and self.x > target_x):
            zwischen_zellen_index.append([(self.x - i,self.y + i) for i in range(1,target_y - self.y)])

        elif (target_y < self.y and self.x < target_x):
            zwischen_zellen_index.append([(self.x + i,self.y - i) for i in range(1,target_y - self.y)])






        print(str(zwischen_zellen_index))
        super().moveTo(target_x, target_y, chess_boar)










