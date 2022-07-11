
def numeroPrimo():
    numero = int(input('Digite un numero: '))

    if(numero>1 and numero%2!=0):
        print('Es Primo')
    elif(numero==2):
        print('Es primo')
    else:
        print('No es primo')    

def anoBisiesto():
    ano = int(input('Digite el año: '))

    if(ano%4==0 and ano%400!=0):
        print('El año es bisiesto')

numeroPrimo()
anoBisiesto()
