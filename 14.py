"""
Crear un programa que pregunte al usuario su nombre, edad,
dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje.
"""

datos_usuario = {
    'nombre': '',
    'edad': 0,
    'dirección': '',
    'teléfono': 0 
}

datos_usuario['nombre'] = input('¿Cuál es tu nombre? ')
datos_usuario['edad'] = int(input('¿Cuántos años tenés? '))
datos_usuario['dirección'] = input('¿Cuál es tu dirección? ')
datos_usuario['teléfono'] = int(input('¿Y tu número de teléfono? '))

print(f"Te llamas {datos_usuario['nombre']}. Tenes {datos_usuario['edad']} años. Tu dirección es {datos_usuario['dirección']} y tu teléfono {datos_usuario['teléfono']}")
