
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


class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def notaFinal(self):
        if self.nota >= 5 and self.nota <= 10:
            print('Alumno: ',self.nombre)
            print("Nota: ",self.nota)
            print("Estado Aprobado")
        elif self.nota < 5:
            print('Alumno: ',self.nombre)
            print("Nota: ",self.nota)
            print("Estado No aprobado")  


nombre = input('Digite su nombre: ')

nota = -1
while (nota < 0 or nota > 10):
    nota = int(input('Digite la nota (0-10): '))


a1 = Alumno(nombre, nota)         
a1.notaFinal()
