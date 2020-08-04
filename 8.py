"""
Pedirle al usuario que ingrese por teclado 3 números binarios 
de 8 bits, para cada uno imprimir su siguiente (número + 1) pero 
en sistema decimal. Recuerden que los números binarios están 
compuestos por 1 y 0.
"""

num_binario = input("Ingrese un número binario de 8 bits: ")
num_decimal = int(num_binario, 2)

print(num_decimal + 1)