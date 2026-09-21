# Tupla con 3 elementos.
# Cada elemento de la tupla es un diccionario con los
# ingredientes de una receta.

recetas = {'Tortilla':{'Huevo','Aceite','Sal'},
    'Pollo con tomate':{'Pollo','Aceite','Sal','Tomate'},
    'Bizcocho':{'Huevo','Harina','Levadura'}}

# Conjunto con productos que tenemos en casa

ingredientes_disponibles = {'Huevo', 'Aceite', 'Sal', 'Levadura'}

# Indicar si se pueden o no realizar las recetas.
for nombre, ingredientes in recetas.items():
    print(nombre, ingredientes.issubset(ingredientes_disponibles))

# Elaborar la lista de la compra con los elementos que faltan.
cesta = set()
for receta in recetas.values():
    cesta.update(receta.difference(ingredientes_disponibles))
print(f'Cesta:{cesta}')