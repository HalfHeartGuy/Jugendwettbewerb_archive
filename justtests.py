















class Sprite():
    def init(self,x:int,y:int,size:int,costume:str,color:str,direction:int):
        self.x = x
        self.y = y
        self.size = size
        self.costume = costume
        self.color = color
        self.direction = direction

    def moveTo(self,target_x,target_y):
        self.x = target_x
        self.y  = target_y

class Chess_Figure(Sprite):
    def __init__(self,x:int,y:int,size:int,costume:str,color:str,direction:int,player:str,status:bool,selected:bool):
        self.x = x
        self.y = y
        self.size = size
        self.costume = costume
        self.color = color
        self.direction = direction
        self.player = player
        self.status = status
        self.selected = selected

class Knight(Chess_Figure):
    def get_allowed_pos(self):
        allowed_pos =  []
        print("current pos: " + str(self.x) + "/" + str(self.y))
        allowed_pos.append([self.x + 1,self.y + 2])
        allowed_pos.append([self.x - 1, self.y + 2])

        allowed_pos.append([self.x + 1, self.y - 2])
        allowed_pos.append([self.x - 1, self.y - 2])

        allowed_pos.append([self.x + 2, self.y - 1])
        allowed_pos.append([self.x + 2, self.y + 1])

        allowed_pos.append([self.x -2, self.y - 1])
        allowed_pos.append([self.x - 2, self.y + 1])
        #for i in range(0,len(allowed_pos)):
         #   print(i)
        for i in allowed_pos:
            if i[0] > 8 or i[0] < 1 or i[1] > 8 or i[1] < 1:
                allowed_pos.remove(i)
        print(allowed_pos)





        print("allowed positions: " + str(allowed_pos))




Figure1 = Knight(0,0,10,"Knight","black",90,"Mokeyandgrooby",True,True)
Knight.get_allowed_pos(Figure1)