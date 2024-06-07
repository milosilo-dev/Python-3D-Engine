from Engine.Main import engine
import pygame

instance = engine()

instance.new_modle_from_obj("/home/miles/Documents/Python/3D Engine/BuiltIn/cube.obj")

running = True

def stop(e):
    running = False
    
def key_down(e):
    if (e.key == pygame.K_w):
        instance.modles[0].angley += 1
    elif (e.key == pygame.K_s):
        instance.modles[0].angley -= 1
    elif (e.key == pygame.K_a):
        instance.modles[0].anglex += 1
    elif (e.key == pygame.K_s):
        instance.modles[0].anglex -= 1

instance.graphics.events.keydown_e  += key_down
instance.graphics.events.quit_e     += stop

while running:
    instance.update()