"""
Crear un programa que pregunte al usuario 5 números enteros
y devuelva una lista con ellos.
"""

numeros = []

for i in range(5):
  numeros.append(int(input("1. Ingresa un numero entero:")))

print(numeros)