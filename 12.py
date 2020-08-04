"""
Crear un programa que almacene los vectores (1,2,3) y (-1,0,2)
en dos listas y muestre por pantalla su producto escalar.
"""

vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]
producto = []

for i in range(3):
    producto.append(vector1[i] * vector2[i])

print(sum(producto))
