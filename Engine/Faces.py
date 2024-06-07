from Engine.Vertex import vertex
import random

class face:
    def __init__(self, Lface, graphics, angle, scale, pos):
        self.graphics = graphics
        self.angle = angle
        self.pos = pos
        
        self.scale_x = scale[0]
        self.scale_y = scale[1]
        self.scale_z = scale[2]
        
        self.z_average = 0
        
        self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        
        self.verts = []
        for vert in Lface:
            self.verts.append(vertex(vert[0], vert[1], vert[2], self.graphics, self.angle, scale, pos))
        self.calculate_screen_points()
    
    def calculate_average_z(self):
        average_z = 0
        for vert in self.verts:
            average_z = average_z + vert.layer
        
        average_z = average_z / len(self.verts)
        self.z_average = average_z
        
    def calculate_screen_points(self):
        for vert in self.verts:
            vert.calculate_screen_points()
            vert.anglex = self.angle[0]
            vert.angley = self.angle[1]
            vert.anglez = self.angle[2]
        self.calculate_average_z()
            
    def draw(self):
        self.graphics.draw_tri((self.verts[0].perspective_x * self.scale_x, self.verts[0].perspective_y * self.scale_y), (self.verts[1].perspective_x * self.scale_x, self.verts[1].perspective_y * self.scale_y), (self.verts[2].perspective_x * self.scale_x, self.verts[2].perspective_y * self.scale_y), self.color)
        for vert in  self.verts:
            vert.draw()