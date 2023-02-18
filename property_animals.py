class Animals:
    def __init__(self, species, age, weight):
        self._species = species
        self._age = age
        self._weight = weight

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, species):
        self._species = species

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight
        
animal = Animals("Cat", 3, 5)
print(animal.species) # "Cat"
print(animal.age) # 3
print(animal.weight) # 5

animal.species = "Dog"
animal.age = 7
animal.weight = 25
print(animal.species) # "Dog"
print(animal.age) # 7
print(animal.weight) # 25