from ursina import *
from ursina.shaders import basic_lighting_shader


    
class   BPiece(Draggable):
    def __init__(self, position = (0,0.6,1), model = 'cube', scale = 0.25):
        super().__init__(
            parent = scene,
            position = position,
            model = model,
            color = color.color(0,0,0.25),
            scale = scale,
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
            lock_z = False,
            lock_y = False,
            lock_x = False,
        )
    def input(self, key):
        if self.hovered and key == 'left mouse down':
            if self.require_key == None or held_keys[self.require_key]:
                self.start_dragging()

        if self.dragging and key == 'left mouse up':
            self.stop_dragging()


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
        self.dragging = False
        self.delta_drag = self.world_position - self.start_pos
        Draggable._z_plane.enabled = False
        self.collision = True
        mouse.traverse_target = scene
        self.x = round(self.x)
        self.z = round(self.z) 

        if hasattr(self, 'drop'):
            self.drop()


    def update(self):
        if self.dragging:
            if mouse.world_point:
                if not self.lock_x:
                    self.world_x = mouse.world_point[0] - self.start_offset[0]
                if not self.lock_y:
                    self.world_y = mouse.world_point[1] - self.start_offset[1]
                if not self.lock_z:
                    self.world_z = mouse.world_point[2] - self.start_offset[2]

            if self.step[0] > 0:
                hor_step = 1/self.step[0]
                self.x = round(self.x * hor_step) /hor_step
            if self.step[1] > 0:
                ver_step = 1/self.step[1]
                self.y = round(self.y * ver_step) /ver_step
            if self.step[2] > 0:
                dep_step = 1/self.step[2]
                self.z = round(self.z * dep_step) /dep_step



## modificaciones para el otro equipo ( cosas de x, z y rotaciones )
class   WPiece(Draggable):
    def __init__(self, position = (0,0.6,1), model = 'cube', scale = 0.25):
        super().__init__(
            parent = scene,
            position = position,
            model = model,
            color = color.color(0,0,0.85),
            scale = scale,
            shader= basic_lighting_shader,
            origin_y = 3,
            highlight_color = color.red,
            rotation = (0,90,0),
            custom_attribute = 0.6,
            plane_direction=( 0,1,0), 
            lock=(0,1,0),
            dragging = False,
            delta_drag = 0,
            start_offset = (0,0,0),
            lock_z = False,
            lock_y = False,
            lock_x = False,
        )
    def input(self, key):
        if self.hovered and key == 'left mouse down':
            if self.require_key == None or held_keys[self.require_key]:
                self.start_dragging()

        if self.dragging and key == 'left mouse up':
            self.stop_dragging()


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
        self.dragging = False
        self.delta_drag = self.world_position - self.start_pos
        Draggable._z_plane.enabled = False
        self.collision = True
        mouse.traverse_target = scene
        self.x = round(self.x)
        self.z = round(self.z) 

        if hasattr(self, 'drop'):
            self.drop()


    def update(self):
        if self.dragging:
            if mouse.world_point:
                if not self.lock_x:
                    self.world_x = mouse.world_point[0] - self.start_offset[0]
                if not self.lock_y:
                    self.world_y = mouse.world_point[1] - self.start_offset[1]
                if not self.lock_z:
                    self.world_z = mouse.world_point[2] - self.start_offset[2]

            if self.step[0] > 0:
                hor_step = 1/self.step[0]
                self.x = round(self.x * hor_step) /hor_step
            if self.step[1] > 0:
                ver_step = 1/self.step[1]
                self.y = round(self.y * ver_step) /ver_step
            if self.step[2] > 0:
                dep_step = 1/self.step[2]
                self.z = round(self.z * dep_step) /dep_step
