paises = input('Digite una lista de paises (separelos por ,) :\n')

listaPaises = paises.split(',')
eliminandoRep = set(listaPaises)
listaPaises = list(eliminandoRep)
ordenListaPaises = sorted(listaPaises) 
print(ordenListaPaises)