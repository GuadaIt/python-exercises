"""
Crear un programa que cree un diccionario vacío y lo vaya
llenado con información sobre una persona (por ejemplo nombre, 
edad, sexo, teléfono, correo electrónico, etc.) que se le 
pida al usuario. Cada vez que se añada un nuevo dato debe 
imprimirse el contenido del diccionario.
"""

información_usuario = {}
continuar = 'y'

while continuar == 'y':
    info = input('Dato a cargar: ')
    valor = input(f"{info}: ")
    información_usuario[info] = valor
    print(información_usuario)
    continuar = input("¿Desea continuar? y/n ").casefold()