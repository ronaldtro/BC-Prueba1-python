inicio = int(input('Digite el valor de inicio: '))
fin = int(input('Digite el valor final: '))

lista = []

for valor in range(inicio, fin):
    if(valor % 2 != 0):
        lista.append(valor)

print('Los numeros impares son: ',lista)