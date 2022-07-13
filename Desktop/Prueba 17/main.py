
from functools import reduce

listaNumeros = [1,2,3,4,5]
print('Lista numeros: ',listaNumeros)

def funcFilter(elem):

    if elem % 2 != 0:
        return True

    return False    

ListImpares = filter(funcFilter, listaNumeros)
ListImpares = list(ListImpares)

print('\nLista impares: ',ListImpares)

def funcRed(a,b):
    return a+b

listaSumada = reduce(funcRed, ListImpares)    
print("\nLa suma de cada elemento de la lista es: ",listaSumada)
