



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


            

def  calculateMyCells(grid_width: int, start_coordinate:tuple, cell_with: 50) -> list[list[tuple]]:
    result = [[(0,0)] * grid_width for i in range(grid_width)]
    #print(result)
    for i in range(grid_width):
        for j in range(grid_width):    
            cell_x= start_coordinate[0] + j * cell_with
            cell_y = start_coordinate[1] - i * cell_with    
            result[i][j] = (cell_x, cell_y)
    return result


myCells = calculateMyCells(6, (-50, -0), 50)



draw_cell_grid(myCells, myNumbers)

line_array_4_4 = [[(0,3),(0,5)],[(0,5),(3, 5)]]

# write a function to draw lines using turtle, for a given list of lines. Each line in this list is a list of tuples. Each tuple represents a point (x,y).
def draw_lines(myCells: list[list[tuple]], lines:list[list[tuple]], color="black" , width=1):
    turtle.speed(10)
    turtle.color(color)
    turtle.width(width)
    for line in lines:
        turtle.penup()

        start_point_idx = line[0] # e.g.(0,3)
        turtle.goto(myCells[start_point_idx[0]][start_point_idx[1]])
        turtle.pendown()

        end_point_idx = line[1] # e.g.(0,5)
        turtle.goto(myCells[end_point_idx[0]][end_point_idx[1]])

    turtle.penup()








draw_lines(myCells,line_array_4_4, "red", 3)
turtle.done()