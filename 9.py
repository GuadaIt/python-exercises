"""
Pedirle al usuario que ingrese el monto disponible en su 
tarjeta de crédito. Evaluar si puede realizar una compra 
de $2500, si puede indicar cuánto saldo le queda luego de 
efectuarla. Si no puede, indicar cuánto dinero le falta para 
poder realizarla.
"""

monto_disponible = int(input("Ingresa el monto disponible de tu tarjeta: "))

if (monto_disponible > 2500):
  print(f"Saldo restante: {monto_disponible - 2500}")
else:
  print(f"Te hacen falta ${2500 - monto_disponible} para realizar la compra")  
