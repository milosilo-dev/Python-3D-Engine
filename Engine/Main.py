from Engine.graphics import Graphics
from Engine.obj2modle import obj2modle

class engine:
    def __init__(self):
        self.graphics = Graphics((0, 0, 0))
        self.modles = []
        
    def new_modle_from_obj(self, PATH):
        self.modles.append(obj2modle(PATH, 3, 3, 0, 0, 0, 0, self.graphics, (100, 100, 100)))
    
    def calculate(self):
        for modle in self.modles:
            modle.calculate_screen_points()
    
    def draw(self):
        for modle in self.modles:
            modle.draw()
            
    def update(self):
        self.graphics.update_front()
        self.calculate()
        self.draw()
        self.graphics.update_back()