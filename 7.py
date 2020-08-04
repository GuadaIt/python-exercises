"""
Crear un diccionario con 5 estudiantes y sus respectivas 
notas. Imprimir por pantalla los alumnos que aprobaron y 
su nota (no en forma de diccionario, si no con nombre : nota).
Tener en cuenta que para aprobar el alumno debe sacarse una 
nota mayor o igual a 7 y menor o igual a 10.
"""

estudiantes = {
  'Mario': 5,
  'Luigi': 8,
  'Popeye': 6,
  'Olivia': 9,
  'Zelda': 8,
  'Goku': 6
}

for key, value in estudiantes.items():
  if (value >= 7):
    if (value <= 10):
        print(f"{key}: {value}")
    else: 
      continue    