
class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    def __init__(self, color, rueda, puertas, velocidad, cilindrada):
        super().__init__(color, rueda, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return  "Color: {} Ruedas: {} Puertas: {} Velocidad: {} Cilindrada: {}".format(self.color, self.ruedas, self.puertas, self.velocidad, self.cilindrada)


c1 = Coche('Rojo', 4, 4, 90, 700)
print(c1)



