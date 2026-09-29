class Animal:
    pass

class AnimalPicorro(Animal):
    pass

alacran = AnimalPicorro()
elefante = Animal()

# issubclass -> Indica si una clase es subclase de otra.
print(issubclass(AnimalPicorro, Animal)) # True
print(issubclass(Animal, AnimalPicorro)) # False
print(issubclass(Animal, object)) # True
print(issubclass(AnimalPicorro, object)) # True