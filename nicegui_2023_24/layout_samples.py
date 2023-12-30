import os.path

from nicegui import ui
from nicegui import *
with ui.grid(columns=3):
    for i in range(9):
        ui.button("Button {}".format(i + 1),on_click =lambda event , i = i:print("Button {} clicked".format(i + 1)))
    dir_path = os.path.dirname(os.path.realpath(__file__))

    image_path = os.path.join(dir_path, "D:\wofproject\wp3932093-wings-of-fire-wallpapers.jpg")
    ui.image(image_path)

    ui.label("lable left")

    ui.label("label right")
ui.run()