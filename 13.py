"""
Crear un programa que guarde en una variable el 
diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al 
usuario por una divisa y muestre su símbolo o un mensaje de 
aviso si la divisa no está en el diccionario.
"""

divisas = {
    'Euro': '€', 
    'Dollar':'$', 
    'Yen':'¥'
}

# lowercase el input del usuario
divisa_input = input('Ingresa una divisa: ').casefold()
# uppercase la primera letra y concatena el resto del string tal cual está
divisa_input = divisa_input[0].upper() + divisa_input[1:]

if divisa_input in divisas:
    print(divisas[divisa_input])
else:
    print('Divisa no encontrada')    