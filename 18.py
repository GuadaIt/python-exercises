"""
Crear una lista con 10 números enteros cualquiera. 
Indicar cuál es el número mayor y cuál es el número menor.
Si al menos hay 3 números mayores a 100, imprimir esos números,
si no, imprimir los números menores a 50 que formen parte de la lista.
"""

num_enteros = [150, 12, 5, 789, 83, 4, 18, 81, 22, 97]
num_enteros.sort()

print(f"Numero mayor: {num_enteros[-1]}")
print(f"Numero menor: {num_enteros[0]}")

mayor_100 = []
menor_50 = []

for num in num_enteros:
  if (num > 100):
      mayor_100.append(num)
  elif (num < 50):
      menor_50.append(num)
  else:
      continue

if (len(mayor_100) > 2):
    for num in mayor_100:
        print(num)
else:
    for num in menor_50:
        print(num)                    
