# Tupla con 3 elementos.
# Cada elemento de la tupla es un conjunto con los
# ingredientes de una receta.

recetas = (
    {'Huevo','Aceite','Sal'},
    {'Pollo','Aceite','Sal','Tomate'},
    {'Huevo','Harina','Levadura'}
)

# Conjunto con productos que tenemos en casa

ingredientes_disponibles = {'Huevo', 'Aceite', 'Sal', 'Levadura'}

# Indicar si se pueden o no realizar las recetas.

for receta in recetas:
    print(receta, receta.issubset(ingredientes_disponibles))
# Elaborar la lista de la compra con los elementos que faltan.
cesta = set()
for receta in recetas:
    cesta.update(receta.difference(ingredientes_disponibles))
print(f'Cesta:{cesta}')