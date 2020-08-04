"""
Escribir un programa que almacene todas las letras del 
abecedario y luego elimine las vocales y nos devuelva 
una lista sin las vocales, sin modificar la original.
"""

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vocales = ['a', 'e', 'i', 'o', 'u']
letras_sin_vocales = []

for i in letras:
  if i in vocales:
    continue
  else:
    letras_sin_vocales.append(i)

print(letras_sin_vocales)