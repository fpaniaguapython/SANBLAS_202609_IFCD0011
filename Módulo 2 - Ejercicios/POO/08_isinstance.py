class Animal:
    pass

class AnimalPicorro(Animal):
    pass

alacran = AnimalPicorro()

# isinstance --> Indica si un objeto es de una clase o no
print(isinstance(alacran, AnimalPicorro)) # True
print(isinstance(alacran, Animal)) # True
print(isinstance(alacran, object)) # True
print(isinstance('abc', str)) # True
print(isinstance('abc', int)) # False
print(isinstance('10', int)) # False