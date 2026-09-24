def calcular_maximo(*listas):
    print(type(listas)) # tuple
    print(listas) # (3, 4, 5, 8, -1, 2)
    return max(listas)

calcular_maximo(3, 4, 5, 8, -1, 2)

def obtener_algo(**kwargs):
    print(type(kwargs)) # dict
    print(kwargs) # {'edad': 20, 'altura': 1.7, 'peso': 95}

obtener_algo(edad=20, altura=1.70, peso=95)