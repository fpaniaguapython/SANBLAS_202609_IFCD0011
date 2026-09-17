def valorar(elemento : tuple) -> int:
    return elemento[1]

hijos_alberto = [('Hanne', 12),('Erwan', 9),
                 ('José María', 25), ('Zoe',4)]

hijos_alberto.sort(key=valorar, reverse=True)
print(hijos_alberto)