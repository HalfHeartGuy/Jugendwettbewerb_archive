import turtle

def draw_cell(x, y, w, num, font_size):
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Set up the turtle for drawing cell
    cell_turtle = turtle.Turtle()
    cell_turtle.speed(10)  # Fastest speed

    # Calculate half width for positioning
    half_width = w / 2

    # Start drawing from the top-left corner
    cell_turtle.penup()
    cell_turtle.goto(x - half_width, y + half_width)
    cell_turtle.pendown()

    # Draw the square cell
    for _ in range(4):
        cell_turtle.forward(w)
        cell_turtle.right(90)

    # Write the number in the middle of the cell
    cell_turtle.penup()
    cell_turtle.goto(x, y - font_size//2)  # Adjusting for font size so number appears centered
    cell_turtle.write(str(num), align="center", font=("Arial", font_size, "normal"))

    # Hide the turtle after drawing
    cell_turtle.hideturtle()
    screen.mainloop()



def draw_cells_row(cells:list, numbers:dict):
    for cell_idx in range(len(cells)):
        x = cells[cell_idx][0]
        y = cells[cell_idx][1]
        zahl = numbers[str(cell_idx) if str(cell_idx) in numbers.keys() else ""]
        draw_cell(x,y,50,zahl,20)


def draw_cell_grid(cells:list[list], numbers:dict):
    for row_idx in range(len(cells)):
        cells_in_row = cells[row_idx]
        draw_cells_row(cells_in_row,numbers[row_idx])




#draw_cells_row([[-50, 0], [0, 0], [50, 0], [100, 0], [150, 0], [200, 0]], {"0": 1, "2": 2, "3": 3})

# Test the function
#draw_cell(0, 0, 100, 3, 30)

myCells = [
    [[-50, 0], [0, 0], [50, 0], [100, 0], [150, 0], [200, 0]],
    [[-50, -50], [0, -50], [50, -50], [100, -50], [150, 0], [200, 0]],
    [[-50, 0], [-150, 0], [-150, 0], [-150, 0], [-150, 0], [-150, 0]],

]

mynumbers = [
    {"0":1,"2":2,"3":4},
    {"2":3,"4":5},
    {"2":1}

]

draw_cell_grid(myCells,mynumbers)
turtle.done()