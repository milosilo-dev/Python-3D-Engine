from Engine.Model import model

def obj2modle(PATH, x_off, y_off, z_off, x_angle, y_angle, z_angle, g, scale):
    f = open(PATH, "r")
    L_model = []
    for line in f:
        L_model.append(line)
    f.close()
    
    v = []
    f = []
    for line in L_model:
        if line[0] == "v" and line[1] == " ":
            cords = line.split(" ")
            cords = (float(cords[1]), float(cords[2]), float(cords[3]))
            v.append(cords)
        elif line[0] == "f" and line[1] == " ":
            face = line.split(" ")
            face = (face[1], face[2], face[3])
            faces = []
            for cord in face:
                cord = cord.split("/")
                cord = v[int(cord[0]) - 1]
                faces.append(cord)
            f.append(faces)
    
    return model(x_off, y_off, z_off, x_angle, y_angle, z_angle, f, g, scale)