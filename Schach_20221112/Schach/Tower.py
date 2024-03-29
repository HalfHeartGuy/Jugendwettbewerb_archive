##from Chess import Chess_Piece, myFuncForChessPiece

from Chess import *

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

    def moveTo(self,target_x:int,target_y:int,chess_boar:list):
        print("jetzt gilt eigene Regeln von Tower")

        zwischen_zellen_index = self.calc_between_position_tower(target_x, target_y)

        print(str(zwischen_zellen_index))
        super().moveTo(target_x,target_y,chess_boar)

def calc_between_position_tower(start_x,start_y, target_x, target_y):
    ## jetzige Position ist (self.x, self.y), target ist (target_x, target_y)
    zwischen_zellen_index = []
    if (target_y > start_y and start_x == target_x):
        zwischen_zellen_index = [(start_x, y) for y in range(start_y + 1, target_y)]
    elif (target_y < start_y and start_x == target_x):
        zwischen_zellen_index = [(start_x, y) for y in range(target_y + 1, start_y)]
    elif (start_y == target_y and start_x < target_x):
        zwischen_zellen_index = [(x, target_y) for x in range(start_x + 1, target_x)]
    elif (start_y == target_y and start_x > target_x):
        zwischen_zellen_index = [(x, target_y) for x in range(target_x + 1, start_x)]
    return zwischen_zellen_index

## von (0,0) zu (0,4) bewegen, welche Zellen sind "Zwischenzellen"?  [(0,1),(0,2),(0,3)]
## von (x,y1) zu (x, y2) bewgen, welche Zellen sind "Zwischenzellen"? [(x, y1 + 1), (x, y1 + 2) ,..., (x, y2 - 1)], y2 > y1
# [(x,y) for y in range(y1+1, y2)] if y2 > y1

