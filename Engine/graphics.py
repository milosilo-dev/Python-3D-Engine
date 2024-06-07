from pygame import init, display, draw, time, event, QUIT, KEYDOWN, KEYUP, quit
from events import Events

class Graphics:
    def __init__(self, bg):
        init()
        self.screen = display.set_mode((1280, 720))
        self.clock = time.Clock()
        self.events = Events()
        self.background = bg
    
    def update_front(self):
        for e in event.get():
            if e.type == QUIT:
                self.events.quit_e(e)
            elif e.type == KEYDOWN:
                self.events.keydown_e(e)
            elif e.type == KEYUP:
                self.events.keyup_e(e)
                    
        self.screen.fill(self.background)
    
    def update_back(self):
        display.flip()

        self.clock.tick(60)
    
    def draw_line(self, pos1, pos2, color, width=1):
        draw.line(self.screen, color, pos1, pos2, width)
        
    def draw_tri(self, pos1, pos2, pos3, color, width=0, fill=False, fill_color=(255, 255, 255)):
        draw.polygon(self.screen, color, (pos1, pos2, pos3), width)
        
    def draw_point(self, pos, color):
        draw.circle(self.screen, color, pos, 1)
        
    def close():
        quit()