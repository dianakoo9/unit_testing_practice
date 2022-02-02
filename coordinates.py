
def on_line(firstCoord,secondCoord,x):
    m = find_slope(firstCoord,secondCoord)
    b = find_yintercept(firstCoord, m)
    y = (m*x) + b
    return y

def find_slope(firstCoord,secondCoord):
    return (secondCoord[1]-firstCoord[1])/(secondCoord[0]-firstCoord[0])

def find_yintercept(coord, slope):
    return coord[1]-(slope*coord[0])
