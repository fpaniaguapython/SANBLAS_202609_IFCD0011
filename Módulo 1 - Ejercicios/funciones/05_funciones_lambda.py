def sumar(x: int, y:int) -> int:
    return x+y

print(sumar(5,3))

funcion_lambda = lambda x, y: x+y
print(funcion_lambda(8,10))

valores = (10, -5, 12, 8, -2, 11, 18)

# Función 'convencional'
def mayor_10(valor):
    return valor>10

valores_mayor_10 = filter(mayor_10, valores)
print(list(valores_mayor_10))

valores_mayor_10 = filter(lambda valor: valor>10, valores)
print(list(valores_mayor_10))