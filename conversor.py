# Solicitamos la cantidad que vamos a convertir a dolares
pesos = input("¿Cual es la cantidad de pesos colombianos que tienes? : ")
# Almacenamos ese valor como una variable de tipo <float>
pesos = float(pesos)

# Este valor nor sirve para convertir de pesos colombianos a dolares usando regla de 3.
valor_dolar = 3875
# Realizamos la conversion
dolares = pesos / valor_dolar

# Ya que nuestro resultado sera de tipo <float>, con el comando round(), indicamos cuantas decimales queremos que muestre en consola del resultado.
dolares = round(dolares, 2)
# Convertimos el valor a texto para concatenarlo mas facil
dolares = str(dolares)
# Mostramos el resultado
print("Tienes $ "+ dolares + " dolares.")