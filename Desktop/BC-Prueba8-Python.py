import math

def areaTriangulo(base, altura):
    return (base*altura)/2

def areaCirculo(radio):
    return math.pi*(radio**2)

print('Area triangulo: ',areaTriangulo(2, 2))
print('Area Circulo: ',areaCirculo(4))