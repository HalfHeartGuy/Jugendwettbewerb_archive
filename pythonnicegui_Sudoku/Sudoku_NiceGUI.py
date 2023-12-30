# bis jetzt nur zeit


import datetime
from nicegui import ui
import sudoku_Matrix as sm
import sudoku_3
from sudoku_3 import *

starttime = None

ui.markdown('## Sudoku Game')
sudoku_numbers = sm.suduku_matrix()



def displaySudokuField(difficulty,sudoku):

    sudoku_numbers = sudoku_3.zerosInSudoku(difficulty,sudoku)

    with ui.grid(columns=3):

        for block_index in range(9):
            show_one_sudoku_block(block_index, one_sudoku_block=sudoku_numbers[block_index])
    toggle1.visible = False


# return sudoku numbers for give culomnIndex
def get_sudoku_numbers_column(columnIndex: int):





    if columnIndex in [0,1,2]:
        return [sudoku_numbers[0][i] for i in range(columnIndex,columnIndex + 7,3)] + [sudoku_numbers[3][i] for i in range(columnIndex,columnIndex + 7,3)] + [sudoku_numbers[6][i] for i in range(columnIndex,columnIndex + 7,3)]
    elif columnIndex in [3,4,5]:
        return [sudoku_numbers[1][i] for i in range(columnIndex % 3,columnIndex + 4,3)] + [sudoku_numbers[4][i] for i in range(columnIndex % 3,columnIndex + 4,3)] + [sudoku_numbers[7][i] for i in range(columnIndex % 3,columnIndex + 4,3)]
    elif columnIndex in [6,7,8]:
        return [sudoku_numbers[2][i] for i in range(columnIndex % 3,columnIndex + 1,3)] + [sudoku_numbers[5][i] for i in range(columnIndex % 3,columnIndex + 1,3)] + [sudoku_numbers[8][i] for i in range(columnIndex % 3,columnIndex + 1,3)]





def get_sudoku_numbers_row(rowIndex: int):
    if rowIndex in [0, 3, 6]:
        return sudoku_numbers[rowIndex - 0][0:3] + sudoku_numbers[rowIndex + 1][0:3] + sudoku_numbers[rowIndex + 2][:3]

    elif rowIndex in [1, 4, 7]:
        return sudoku_numbers[rowIndex - 1][3:6] + sudoku_numbers[rowIndex][3:6] + sudoku_numbers[rowIndex + 1][3:6]

    elif rowIndex in [2, 5, 8]:
        return sudoku_numbers[rowIndex - 2][6:9] + sudoku_numbers[rowIndex - 1][6:9] + sudoku_numbers[rowIndex][6:9]


label = ui.label().classes('absolute top-0 right-0')


def updateBlock(new_value: str, i: int, block_index: int):
    print(f"new Value: {new_value} at position {i} in block at {block_index}.")

    sudoku_numbers[block_index][i] = int(new_value)


# Aufgabe 1: reset timer
def start_timer(button):
    global starttime
    starttime = datetime.datetime.now()
    ui.timer(1.0, timer)

def timer():
    if starttime is not None:
        diff = datetime.datetime.now() - starttime
        past = int(diff.total_seconds())
        label.set_text(f"Gaming time: {past} seconds")


def isUnique(new_value: str, block_index: int):
    print(f"Validate new Value: {new_value} in block {sudoku_numbers[block_index]}.")
    valdiate_result = sudoku_numbers[block_index].count(int(new_value)) == 1
    print(f"Validate result: {valdiate_result}.")
    return valdiate_result


def show_one_sudoku_block(block_index, one_sudoku_block=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
    with ui.grid(columns=3):
        for i in range(9):
            ui.input(value=one_sudoku_block[i],
                     on_change=lambda inputevent, i=i: updateBlock(str(inputevent.value), i, block_index),
                     validation={"found duplicate": lambda inputevent: isUnique(inputevent, block_index)})



toggle1 = ui.toggle([0,"easy","medium","hard"], value=0,on_change=lambda : displaySudokuField(toggle1.value,sudoku_numbers))

start_button = ui.button("Start Sudoku Game", on_click=start_timer)

ui.run()
# Vorbereitung: Fertig mit der Methode get_sudoku_numbers_colmn.

# Aufgaben für nächste Woche bis 20.12.2023:
# 1. Baue ein selectbox mit 3 Schwierigkeitsstufen: easy(0), medium(1), hard(2), mit default value "easy".

# 2. Nach dem Starten des Spiels, soll 
# 2.1.die Zeit gestartet werden, 
# 2.2(optional). die selectbox verschwinden.
# 2.3. sudoku_numbers mit entsprechenden Placeholder 0 initialisiert werden. 
# Easy bedeutet 37-40 Zahle sind vorgegeben, Medium 32-36, Hard 27-31.

# 3. Wenn alle Lücken in Sudoku gefüllt sind, soll die Zeit gestoppt werden, und dann
# ein großer Text zusammen mit der benötigten Zeit in niceGui ausgegeben werden. Z.B:
# "Congratulations! You have solved the easy Sudoku after 90 seconds!"