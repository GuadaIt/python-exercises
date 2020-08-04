"""
Escribir un programa que seleccione una operación de cuatro 
operaciones numéricas disponibles, una vez seleccionada la 
operación, introducir dos números y ejecutar la operación.
"""
import random

operaciones = ['multiplicacion', 'suma', 'resta', 'division']

index = random.randrange(0, 4)

num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese un número: '))

if (operaciones[index] == 'multiplicacion'):
    print(num1 * num2)
elif (operaciones[index] == 'suma'):
    print(num1 + num2)
elif (operaciones[index] == 'resta'):
    print(num1 - num2)
else:
    print(num1 / num2)            