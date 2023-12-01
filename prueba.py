from ursina import *
from ursina.shaders import basic_lighting_shader
from table2 import Piece
app = Ursina()
Entity(model='plane', scale=8, texture='white_cube', texture_scale=(8,8), position =(0.5,0,0.5))
EditorCamera(rotation=(30,10,0))
class Cuadrado(Entity):
    def __init__(self, equipo, position):
        super().__init__(
            model='cube',
            position = position,
            color=color.red if equipo == 'equipo1' else color.blue,
            scale=1,
        )
        self.equipo = equipo
        

equipos = ['w', 'b']
posicion = [0,7]
turno_actual = 0

cuadrados = [
    Piece(position=(i-3,0.8,4), team = 'w', vglobal=turno_actual)  for i in range(8)
]
cuadraDos = [
    Piece(position=(i-3,0.8,-3), team = 'b', vglobal=turno_actual)  for i in range(8)
]

cuadrados.extend(cuadraDos)


app.run()