import pickle


class Vehiculo:

    def __init__(self):
        self.marca = 'Toyota'
        self.color = 'Rojo'
        self.tipo = 'Camioneta'

    def __str__(self):
        return f'marca: {self.marca} color: {self.color} tipo: {self.tipo}'        

v1 = Vehiculo()
fichero = open('vehiculo.bin', 'wb')
pickle.dump(v1, fichero)
fichero.close()

fichero = open('vehiculo.bin','rb')
resultado = pickle.load(fichero)
fichero.close()

print(resultado)

