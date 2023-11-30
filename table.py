from ursina import *
from ursina.shaders import basic_lighting_shader



class   BPiece(Draggable):
    def __init__(self, position = (0,0.6,1), model = None, scale = 0.25):
        super().__init__(
            parent = scene,
            model = model,
            color = color.color(0,0,0.2),
            texture = None,
            position = position,
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
            custom_atribute = 'b',
            custom_atributeX = position[0],
            custom_atributeZ = position[2],
            start_offset = (0,0,0),
            lock_z = False,
            lock_y = False,
            lock_x = False,
            max_x= 7,
            max_z = 7,
            min_x = 0,
            min_z = 0,
        )
    def input(self, key):
        if self.hovered and key == 'left mouse down':
            if self.require_key == None or held_keys[self.require_key]:
                self.start_dragging()
                
                self.animate_y(3, duration= 0.4 )
                self.piece = Entity (position = (0,0,0), model='cube', parent = self, max_y = 0, scale = 3.5)
                self.piece.animate_y(-4.5, duration=0)
                self.piece.animate_y(-11, duration=0.4)

        if self.dragging and key == 'left mouse up':
            self.stop_dragging()
            self.custom_atributeX = self.x
            self.custom_atributeZ = self.z
            print(self.custom_atributeZ)
            entities_to_remove = [entity for entity in scene.entities 
                                  if   getattr(entity, 'custom_atribute', None) == 'w'
                                  and  getattr(entity, 'custom_atributeX', None) == self.custom_atributeX
                                  and  getattr(entity, 'custom_atributeZ', None) == self.custom_atributeZ]
            for entity in entities_to_remove:
                destroy(entity)
                exp = Animation('assets\gifts\explotion-explode.gif', position = (self.x, 1, self.z), loop = False, rotation= (0,-180,0))
                exp2 = Animation('assets\gifts\explotion-explode.gif', position = (self.x, 1, self.z), loop = False)
                destroy(exp, delay = exp.duration)
                destroy(exp2, delay = exp2.duration)
            destroy(self.piece)


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
        self.animate_y(1.35, duration= 0.1)
        self.x = round(self.x)
        self.z = round(self.z) 

        if hasattr(self, 'drop'):
            self.drop()
            

## modificaciones para el otro equipo ( cosas de x, z y rotaciones )
class   WPiece(Draggable):
    def __init__(self, position = (0,0.6,1), model = 'cube', scale = 0.25):
        super().__init__(
            parent = scene,
            model = model,
            texture = None,
            position = position,
            scale = scale,
            shader= basic_lighting_shader,
            origin_y = 3,
            highlight_color = color.red,
            plane_direction=( 0,1,0), 
            lock=(0,1,0),
            dragging = False,
            delta_drag = 0,
            start_offset = (0,0,0),
            lock_z = False,
            lock_y = False,
            lock_x = False,
            max_x= 7,
            max_z = 7,
            min_x = 0,
            min_z = 0,
            custom_atribute =  'w',
            custom_atributeX = position[0],
            custom_atributeZ = position[2],
            rotation = (0,90,0),
            color = color.color(0,0,0.85),
        )
    def input(self, key):
        if self.hovered and key == 'left mouse down':
            if self.require_key == None or held_keys[self.require_key]:
                self.start_dragging()
                
                self.animate_y(3, duration= 0.4 )
                self.piece = Entity (position = (0,0,0), model='cube', parent = self, max_y = 0, scale = 3.5)
                self.piece.animate_y(-4.5, duration=0)
                self.piece.animate_y(-11, duration=0.4)

        if self.dragging and key == 'left mouse up':
            self.stop_dragging()
            self.custom_atributeX = self.x
            self.custom_atributeZ = self.z
            entities_to_remove = [entity for entity in scene.entities 
                                  if   getattr(entity, 'custom_atribute', None) == 'b'
                                  and  getattr(entity, 'custom_atributeX', None) == self.custom_atributeX
                                  and  getattr(entity, 'custom_atributeZ', None) == self.custom_atributeZ]
            for entity in entities_to_remove:
                destroy(entity)
                exp = Animation('assets\gifts\explotion-explode.gif', position = (self.x, 1, self.z), loop = False, rotation= (0,-180,0))
                exp2 = Animation('assets\gifts\explotion-explode.gif', position = (self.x, 1, self.z), loop = False)
                destroy(exp, delay = exp.duration)
                destroy(exp2, delay = exp2.duration)
            destroy(self.piece)

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
        self.animate_y(1.35, duration= 0.1)
        self.x = round(self.x)
        self.z = round(self.z) 

        if hasattr(self, 'drop'):
            self.drop()
            