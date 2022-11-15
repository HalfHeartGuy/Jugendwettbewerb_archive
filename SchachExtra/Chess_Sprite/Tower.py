from Chess import  Chess_Piece, myFuncForChessPiece

class Chess_Piece_Tower(Chess_Piece):
    def __init__(self,name:str,x:int,y:int,size:int,costume:str,color:str,direction:int,player:str,status:bool,selected_by_player:bool):
        super().__init__(name,x,y,size,costume,color,direction,player,status,selected_by_player)

    def get_allowed_positions(self):
        print("{} has a current pos ({},{})".format(self.name,self.x,self.y))
        result = []
        for i in range(1,9):
            result.append([self.x - i,self.y])
            result.append([self.x + i,self.y])
            result.append([self.x,self.y + i])
            result.append([self.x,self.y - i])

        result = filter(myFuncForChessPiece,result)
        return result


    def moveTo(self,target_x:int,target_y:int,chess_board:list):
        print("jetzt gilt eigene Regeln von Tower.")

        #jetzige Position ist (self.x,self.y),target ist (target_x,target_y)

        zwischen_zeilen_index = []
        if (target_y > self.y and self.x == target_x):
            zwischen_zeilen_index = [(self.x,y) for y in range(self.y + 1,target_y)]

        elif (target_y < self.y and self.x == target_x):
            zwischen_zeilen_index = [(self.x,y) for y in range(target_y + 1,self.y)]

        elif (self.y == target_y and self.x < target_x):
            zwischen_zeilen_index = [(x,target_y) for x in range(self.x + 1,target_x)]
        elif (self.y == target_y and self.x < target_x):
            zwischen_zeilen_index = [(x,target_y) for x in range(self.x,target_x + 1)]

        print(str(zwischen_zeilen_index))

        super().moveTo(target_x,target_y,chess_board)
## von (0,0) zu (0,4) bewegen,welche Zeilen sind "Zwischenzeilen"= [(0,1),(0,2),(0,3),(0,4)]
# von (x,y1) zu (x,y2) bewegen,welcge Zeilen sind "Zwischenzeilen"? [(x,y1 + 1),(x,y1 + 2 , ..... , (x,y2 - 1 )],y2 > y
# [[x,y) for y in range(y1 + 1)] if y2 = y1


