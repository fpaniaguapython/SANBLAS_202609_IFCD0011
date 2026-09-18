x = 10
y = x
print(x, y) # 10 10
x = 15
print(x, y) # 15 10

a = 'patata'
b = a
print(a, b) # patata patata
a = 'cebolla'
print(a, b) # cebolla patata

lista_1 = [1, 2]
lista_2 = lista_1
print(lista_1, lista_2) # [1, 2] [1, 2]
lista_1[0]=4
print(lista_1, lista_2) # [4, 2] [4, 2]

lista_1 = [1, 2]
lista_2 = lista_1[:]
print(lista_1, lista_2) # [1, 2] [1, 2]
lista_1[0]=4
print(lista_1, lista_2) # [4, 2] [1, 2]

lista_1 = [1, 2, [3, 4]]
lista_2 = lista_1[:]
print(lista_1, lista_2) # [1, 2, [3, 4]] [1, 2, [3, 4]]
lista_1[0]=5
print(lista_1, lista_2) # [5, 2, [3, 4]] [1, 2, [3, 4]]
lista_1[2][0]=6
print(lista_1, lista_2) # [5, 2, [6, 4]] [1, 2, [6, 4]]

import copy
lista_1 = [1, 2, [3, 4]]
lista_2 = copy.deepcopy(lista_1) # Crea una copia independiente de lista_1


