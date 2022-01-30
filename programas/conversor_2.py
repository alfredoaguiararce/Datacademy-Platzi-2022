menu = """
Bienvenido al conversor de monedas 

1 - Pesos colombianos. 
2-  Pesos argentinos.
3 - Pesos mexicanos.

Elige una opción:  
"""

# Solicitamos que indique el cambio de divisa que desea realizar
opcion = int(input(menu))

if opcion == 1:
    # 1 dolar = 3875 pesos colombianos.
    valor_dolar = 3875
    mensaje = "¿Cuantos pesos colombianos tienes?: "

elif opcion == 2:
    # 1 dolar = 65 pesos argentinos.
    valor_dolar = 65
    mensaje = "¿Cuantos pesos argentinos tienes?: "

elif opcion == 3:
    # 1 dolar = 24 pesos mexicanos.
    valor_dolar = 24
    mensaje = "¿Cuantos pesos mexicanos tienes?: "

else:
    print("Ingresa una opcion correcta")
    mensaje = None
    
if mensaje is not None:
    pesos = float(input(mensaje))
    dolares = round(pesos / valor_dolar, 2)
    print(f"Tienes $ {dolares} dolares")
