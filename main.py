from ursina import *
from terrain import *
from pieces import *

app = Ursina()

button = Button(text = 'jugar', scale = 0.4, position= (0,-0.2,0))
title = Button( text='Ajedrez 2 omggggg', color = color.green, scale_y = 0.2,  position= (0,0.2,0))
background = Entity(model='cube' , texture = 'assets/imgs/background' ,position= (0,0,0),scale_x= 15, scale_y=10)
def game():
    EditorCamera(position = (3.5,3, 3.5))
    Sky()
    terrain()
    pieces()
    destroy(button)
    destroy(title)
    destroy(background)

button.on_click = game
app.run()