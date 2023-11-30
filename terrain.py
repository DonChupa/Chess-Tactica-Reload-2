from ursina import *
from ursina.shaders import basic_lighting_shader
def terrain():
    def tablero():
        for x in range(8):
            for z in range(8):
                if x%2 == 0 and z%2 == 0:
                    cubo = Entity(model="cube", collider="cube", scale= 1, position=(x ,0.1,z), texture="White_cube", color= color.black, shader= basic_lighting_shader)
                elif x%2 != 0 and z%2 != 0:
                    cubo = Entity(model="cube", collider="cube", scale= 1, position=(x  ,0.1,z), texture="White_cube", color= color.black, shader= basic_lighting_shader)
                else:
                    cubo = Entity(model="cube", collider="cube", scale= 1, position=(x  ,0.1,z), texture="White_cube", shader= basic_lighting_shader)

    castle = Entity(model="assets/terreno/castle/scene",  scale = 0.005, position= (3.5  ,-6,3.5) , shader= basic_lighting_shader)
    table = Entity(model="assets/terreno/table/scene.gltf",  scale = 0.07, position= (3.5  ,-6,3.5), shader= basic_lighting_shader)
    tablero()