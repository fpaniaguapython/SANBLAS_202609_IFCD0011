ingredientes = ['Harina', 'Leche', 'Huevo', 'Vino', 'Sal']

# Versión tradicional
mayusculas = []
for ingrediente in ingredientes:
    mayusculas.append(ingrediente.upper())

print(mayusculas)

# Comprensión de lista
ingredientes_mayusculas = [ingrediente.upper() for ingrediente in ingredientes] 
print(ingredientes_mayusculas)