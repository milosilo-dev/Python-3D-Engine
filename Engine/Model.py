from Engine.Faces import face

class model:
    def __init__(self, x, y, z, anglex, angley, anglez, faces, graphics, scale):
        self.num_faces = len(faces)
        self.graphics = graphics
        
        self.faces = []
        for Lface in faces:
            self.faces.append(face(Lface, graphics, (anglex, angley, anglez), scale, (x, y, z)))
        
        self.x = x
        self.y = y
        self.z = z
        self.anglex = anglex
        self.angley = angley
        self.anglez = anglez
    
    def sort_faces(self):
        for n in range(len(self.faces)-1, 0, -1):
            swapped = False
            for i in range(n):
                if self.faces[i].z_average > self.faces[i + 1].z_average:
                    swapped = True
                    self.faces[i], self.faces[i + 1] = self.faces[i + 1], self.faces[i]
            if not swapped:
                return
    
    def calculate_screen_points(self):
        for f in self.faces:
            f.calculate_screen_points()
            f.angle = (self.anglex, self.angley, self.anglez)
        self.sort_faces()
            
    def draw(self):
        for f in self.faces:
            f.draw()