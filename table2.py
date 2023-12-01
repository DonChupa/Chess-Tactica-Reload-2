from ursina import *
from ursina.shaders import basic_lighting_shader



class   Piece(Draggable):
    def __init__(self, position = (0,0.6,1),pieceType='pawn', team='w', vglobal=0):
        super().__init__(
            parent = scene,
            vglobal = vglobal,
            team = team,
            position = position,
            model = f'assets/fichas/{pieceType}/scene.gltf',
            color = color.color(0,0,0.25) if team == 'b'else color.color(0,0,0.8),
            scale = 0.25,
            shader= basic_lighting_shader,
            origin_y = 3,
            highlight_color = color.red,
            rotation = (0,-90,0),
            custom_attribute = 0.6,
            plane_direction=( 0,1,0), 
            lock=(0,1,0),
            dragging = False,
            delta_drag = 0,
            start_offset = (0,0,0),
        )
    def input(self, key):
        if self.hovered and key == 'left mouse down':
            if (self.team == 'w' and self.vglobal == 0) or (self.team == 'b' and self.vglobal == 1):
                self.start_dragging()
            else:
                print(f'turno del rival, {self.vglobal}')

        if self.dragging and key == 'left mouse up':
            self.stop_dragging()
    def cambiarVglobal(self, valor):
        self.vglobal = valor
    def llamar_a_todas_las_pieces(self):
        for entity in scene.entities:
            if isinstance(entity, Piece):
                entity.cambiarVglobal(self.vglobal)
    def start_dragging(self):
        Draggable._z_plane.world_position = mouse.world_point
        Draggable._z_plane.look_at(Draggable._z_plane.position - Vec3(*self.plane_direction))
        if self.has_ancestor(camera.ui):
            Draggable._z_plane.world_parent = camera.ui
        else:
            Draggable._z_plane.world_parent = scene

        self.start_offset = mouse.world_point - self.world_position
        self.dragging = True
        self.start_pos = self.world_position
        self.collision = False
        Draggable._z_plane.enabled = True
        mouse.traverse_target = Draggable._z_plane
        try:
            self.drag()
        except:
            pass


    def stop_dragging(self):
        self.vglobal = (self.vglobal + 1) % 2
        self.llamar_a_todas_las_pieces()
        print(f'turno equipo {self.vglobal}')
        self.dragging = False
        self.delta_drag = self.world_position - self.start_pos
        Draggable._z_plane.enabled = False
        self.collision = True
        mouse.traverse_target = scene
        self.x = round(self.x)
        self.z = round(self.z) 
