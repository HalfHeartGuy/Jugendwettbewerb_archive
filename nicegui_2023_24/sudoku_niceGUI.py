from nicegui import ui



sudoku_numbers = [1,2,3,4,5,6,7,8,9]
ui.markdown("**Sudoku Game**")


with ui.grid(columns=3):
    for i in range(len(sudoku_numbers)):
        ui.number(placeholder="0", value= sudoku_numbers[i], min=1, max=9, step=1)

ui.run()