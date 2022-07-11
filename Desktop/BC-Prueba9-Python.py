
def numeroPrimo(numero):
    if(numero>1 and numero%2!=0):
        return 'Es Primo'
    elif(numero==2):
        return 'Es primo'    

    return 'No es primo'    

numero = int(input('Digite un numero: '))
print('El numero: ',numeroPrimo(numero))
