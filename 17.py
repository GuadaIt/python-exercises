"""
Pedir al usuario que ingrese un mensaje cualquiera, 
si el mensaje tiene más de 100 caracteres imprimirlo por 
pantalla, si tiene entre 50 y 100 caracteres imprimirlo 
al revés, si no se cumple ninguna de las opciones anteriores, 
por pantalla devolver un mensaje que diga "su mensaje es demasiado corto".
"""

mensaje_cualquiera = input("Ingrese un mensaje cualquier: ")

if len(mensaje_cualquiera) > 100:
    print(mensaje_cualquiera)
elif len(mensaje_cualquiera) > 50:
    mensaje_invertido = ''
    for caracter in mensaje_cualquiera:
        mensaje_invertido = caracter + mensaje_invertido
    print(mensaje_invertido)
else:
    print("Su mensaje es demasiado corto")
