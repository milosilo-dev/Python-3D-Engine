from Engine.Matrix import translate, rotateXMatrix, rotateYMatrix, rotateZMatrix

class vertex:
    def __init__(self, x, y, z, graphics, angle, scale, pos):
        self.x = x
        self.y = y
        self.z = z
        
        self.pos = pos
        
        self.anglex = angle[0]
        self.angley = angle[1]
        self.anglez = angle[2]
        
        self.scale_x = scale[0]
        self.scale_y = scale[1]
        self.scale_z = scale[2]
        
        self.perspective_x = 0
        self.perspective_y = 0
        
        self.layer = 0
        
        self.graphics = graphics
    
    def calculate_screen_points(self):
        Ly, Lx, Lz = rotateXMatrix(self.x + self.pos[0], self.y + self.pos[1], self.z + self.pos[2], self.anglex)
        Ly, Lx, Lz = rotateYMatrix(Lx, Ly, Lz, self.angley)
        Ly, Lx, Lz = rotateZMatrix(Lx, Ly, Lz, self.anglez)
        
        self.layer = Lz
        self.perspective_x, self.perspective_y = translate(Ly, Lx, Lz)
        
    def draw(self):
        self.graphics.draw_point((self.perspective_x * self.scale_x, self.perspective_y * self.scale_y), (255, 0, 0))
        
        