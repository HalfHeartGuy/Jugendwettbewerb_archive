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

    return result[0] < 9 and result[0] > 0 and result[1] < 9 and result[1] > 0



class Chess_Piece(Sprite):
    def __init__(self,name:str,x:int,y:int,size:int,costume:str,color:str,direction:int,player:str,status:bool,selected_by_player:bool):
        super().__init__(name,x,y,size,costume,color,direction)
        self.player = player
        self.status = status
        self.selected_by_player = selected_by_player

    def moveTo(self,x,y):

        if [x,y] in self.get_allowed_positions():
            self.x = x
            self.y = y
            print("Chess is moved to [{},{}]".format(x,y))
        else:
            print("Chess can not be moved to [{},{}]".format(x,y))











    #gibt an,welche positionen darf ein ausgewählte Figur im nächsten Schritt belegen.
    #Type dieser Funktion ist Liste von Tupeln,e.g. [(3,5),(4,4),...}
    def get_allowed_positions(self):
        pass
    def defeat(self,enemy_piece_name:str):
        pass



class Chess_Piece_Knight(Chess_Piece):
    def __init__(self,name:str,x:int,y:int,size:int,costume:str,color:str,direction:int,player:str,status:bool,selected_by_player:bool):
        super().__init__(name,x,y,size,costume,color,direction,player,status,selected_by_player)

    def get_allowed_positions(self):
        print("{} has a current pos ({},{})".format(self.name,self.x,self.y))

        result = []
        result.append([self.x - 1,self.y - 2])
        result.append([self.x + 1,self.y - 2])
        result.append([self.x + 1,self.y + 2])
        result.append([self.x - 1,self.y + 2])

        result.append([self.x + 2,self.y + 1])
        result.append([self.x + 2,self.y - 1])
        result.append([self.x - 2,self.y - 1])
        result.append([self.x - 2,self.y + 1])
        result = filter(myFuncForChessPiece,result)

        print("allowed  knight position for next move:")
        resultforreturn = []
        for oneitem in result:
            print(oneitem)
            resultforreturn.append(oneitem)
        return resultforreturn



        #filter all positions with x,y out of range(1,9)
        #for one_pos in result:









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
        print("allowed  tower position for next move:")

        resultforreturn = []


        for oneitem in result:
            print(oneitem)
            resultforreturn.append(oneitem)




        return resultforreturn






knight = Chess_Piece_Knight(name="Knight",x=1,y=1,size=2,costume="1",color="black",direction=90,player="black",status=True,selected_by_player=False)
positionsForKnight = knight.get_allowed_positions()
knight.moveTo(2,3)





tower = Chess_Piece_Tower(name="Tower",x=6,y=6,size=2,costume="1",color="black",direction=90,player="black",status=True,selected_by_player=False)
positionsForTower = tower.get_allowed_positions()


tower.moveTo(8,8)




