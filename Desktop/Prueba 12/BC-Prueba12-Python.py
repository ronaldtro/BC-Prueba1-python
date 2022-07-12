from calculadora import sumar,restar,multiplicar,dividir

numero1 = int(input('Digite el primer numero: '))
numero2 = int(input('Digite el segundo numero: '))

print('El resultado de la suma es: ',sumar.suma(numero1, numero2))
print('El resultado de la resta es: ',restar.resta(numero1, numero2))
print('El resultado de la multiplicacion es: ',multiplicar.multiplicacion(numero1, numero2))
print('El resultado de la division es: ',dividir.division(numero1, numero2))