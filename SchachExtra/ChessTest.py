from Knight import *
from Tower import *
from Bishop import *
from Queen import *
from King import *




knight = Chess_Piece_Knight(name="Knight",x=2,y=1,size=2,costume="1",color="black",direction=90,player="black",status=True,selected_by_player=False)
knight.moveTo(1,3)
'''
tower = Chess_Piece_Tower(name="Tower",x=6,y=6,size=2,costume="1",color="black",direction=90,player="black",status=True,selected_by_player=False)
tower.moveTo(3,6)
tower.moveTo(2,2)


bishop = Chess_Piece_Bishop(name="whiteBishop",x=3,y=1,size=2,costume="1",color="white",direction=90,player="black",status=True,selected_by_player=False)
bishop.moveTo(3,3)#
bishop.moveTo(2,2)
bishop.moveTo(-1,-1)


queen = Chess_Piece_Queen(name="queen",x=4,y=1,size=2,costume="1",color="white",direction=90,player="black",status=True,selected_by_player=False)
queen.moveTo(2, 2)
queen.moveTo(5, 2)

king = Chess_Piece_King(name="queen",x=5,y=1,size=2,costume="1",color="white",direction=90,player="black",status=True,selected_by_player=False)
king.moveTo(5,2)
king.moveTo(6,2)
king.moveTo(5,3)
king.moveTo(5,4)
'''