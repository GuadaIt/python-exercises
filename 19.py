"""
Pedir al usuario que ingrese por teclado 2 números, 
si el primero es menor que el segundo imprimir la resta 
entre el segundo y el primero, si el primero es mayor que
el segundo imprimir la suma de ambos, y si son iguales 
imprimir su producto.
"""

num1 = int(input('1. Ingrese un número: '))
num2 = int(input('2. Ingrese otro número: '))

if (num1 < num2):
    print(num2 - num1)
elif (num1 > num2):
    print(num1 + num2)
else:
    print(num1 * num2)        
