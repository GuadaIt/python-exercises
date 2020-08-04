"""
Ingresar 6 números por teclado, preferentemente enteros, 
ordenarlos de manera creciente e imprimirlos por pantalla.
"""
numeros = []

for i in range(6):
    numeros.append(int(input('Ingresa un número ')))

numeros.sort()
print(numeros)
