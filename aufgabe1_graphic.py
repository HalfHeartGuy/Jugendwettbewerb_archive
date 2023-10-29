


import turtle


'''


1 0 2 4 x x


0 0 3 0 5 x


0 0 1 0 x x


0 0 0 0 x 4


0 2 0 0 x 0


0 0 0 3 x 5


'''




# Write a function to draw a cell using turtle, for a given x,y for middle point and given cell width w.


# in the middle of the cell write a given number with given size.



def draw_cell(x,y,w, number):
    turtle.speed(10)


    turtle.penup()

    turtle.goto(x,y)

    turtle.pendown()

    turtle.write(number)



    turtle.penup()

    turtle.goto(x-w/2,y-w/2)


    turtle.pendown()
    turtle.forward(w)


    turtle.left(90)
    turtle.forward(w)


    turtle.left(90)
    turtle.forward(w)


    turtle.left(90)
    turtle.forward(w)


    turtle.left(90)


    turtle.penup()



# Draw cells for a given list of (x,y) using function draw_cell.


def draw_cells_row(cells:list, numbers:dict):
    for cell_idx in range(len(cells)):
        x = cells[cell_idx][0]
        y = cells[cell_idx][1]
        zahl = numbers[str(cell_idx)] if str(cell_idx) in numbers.keys() else ""

        draw_cell(x, y, 50, zahl)



def draw_cell_grid(cells:list[list], numbers:list[dict]):
    for row_idx in range(len(cells)):
        cells_in_row = cells[row_idx]
        draw_cells_row(cells_in_row, numbers[row_idx])

#draw_cell(0,0, 50, 5)

#draw_cells_row([(-50,0),(-0,0),(50,0),(100,0),(150,0),(200,0)], {"0":1,  "2":2, "3":4})

myCells  = [
            [(-50,0),(-0,0),(50,0),(100,0),(150,0),(200,0)],
            [(-50,-50),(0,-50),(50,-50),(100,-50),(150,-50),(200,-50)],
            [(-50,-100),(0,-100),(50,-100),(100,-100),(150,-100),(200,-100)],
            [(-50,-150),(0,-150),(50,-150),(100,-150),(150,-150),(200,-150)],
            [(-50,-200),(0,-200),(50,-200),(100,-200),(150,-200),(200,-200)],
            [(-50,-250),(0,-250),(50,-250),(100,-250),(150,-250),(200,- 250)]

]
            


myNumbers = [
            {"0":1,  "2":2, "3":4},
            {"2":3, "4":5},
            {"2":1, },
            {"5":4},
            {"1":2},
            {"3":3,"5":5}
]

draw_cell_grid(myCells, myNumbers)

def draw_lines(lines:list[list[tuple]],mycells: list[list[tuple]], color = "red",width = 1):
    turtle.color(color)
    turtle.width(width)
    for line in lines:
        turtle.penup()

        start_point_idx = line[0]
        turtle.goto(line[mycells[start_point_idx]])
        turtle.pendown()
        turtle.goto(line[1])



line_array_4_4 = [[(100,0),(200,0)], [(200,0),(200,-150)]]


draw_lines(line_array_4_4)


turtle.done()
