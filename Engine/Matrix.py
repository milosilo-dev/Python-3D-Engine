import numpy as np
import math

def translate(x, y, z):
    translation = [[1, 0, 0],
                   [0, 1, 0]]
    pos = [x, y, z]
    return np.matmul(translation, pos)

def rotateXMatrix(x, y, z, angle):
    rotation_x = [[1, 0, 0],
                  [0, math.cos(angle), -math.sin(angle)],
                  [0, math.sin(angle), math.cos(angle)]]
    pos = [x, y, z]
    return np.matmul(rotation_x, pos)

def rotateYMatrix(x, y, z, angle):
    rotation_y = [[math.cos(angle), 0, -math.sin(angle)],
                  [0, 1, 0],
                  [math.sin(angle), 0, math.cos(angle)]]
    pos = [x, y, z]
    
    return np.matmul(rotation_y, pos)

def rotateZMatrix(x, y, z, angle):
    rotation_z = [[math.cos(angle), -math.sin(angle), 0],
                  [math.sin(angle), math.cos(angle), 0],
                  [0, 0 ,1]]
    pos = [x, y, z]
    
    return np.matmul(rotation_z, pos)