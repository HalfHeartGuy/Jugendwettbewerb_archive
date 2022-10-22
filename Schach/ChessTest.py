from Knight import *
from Tower import *
from Bishop import *
from Queen import *
from King import *



knight = Chess_Piece_Knight(name="Knight",x=1,y=1,size=2,costume="1",color="black",direction=90,player="black",status=True,selected_by_player=False)
knight.moveTo(3,2)
tower = Chess_Piece_Tower(name="Tower",x=6,y=6,size=2,costume="1",color="black",direction=90,player="black",status=True,selected_by_player=False)

tower.moveTo(3,6)
tower.moveTo(2,2)

bishop = Chess_Piece_Bishop(name="Bishop",x=3,y=1,size=2,costume="1",color="black",direction=90,player="black",status=True,selected_by_player=False)
bishop.moveTo(5,3)

quenn = Chess_Piece_Queen(name="Queen",x=4,y=1,size=2,costume="1",color="black",direction=90,player="black",status=True,selected_by_player=False)
quenn.moveTo(1,1)
quenn.moveTo(2,2)

king = Chess_Piece_King(name="King",x=5,y=1,size=2,costume="1",color="black",direction=90,player="black",status=True,selected_by_player=False)
king.moveTo(5,2)
king.moveTo(6,2)
king.moveTo(5,3)
king.moveTo(5,4)
