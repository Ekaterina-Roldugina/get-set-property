class Animals:
    def __init__(self, species, age, weight):
        self._species = species
        self._age = age
        self._weight = weight

    
    def get_species(self):
        return self._species

    
    def set_species(self, species):
        self._species = species

    
    def get_age(self):
        return self._age

    
    def set_age(self, age):
        self._age = age

    
    def get_weight(self):
        return self._weight

    
    def set_weight(self, weight):
        self._weight = weight
        
        
animal = Animals("Cat", 3, 5)
print(animal._species)
print(animal._age)
print(animal._weight) 

animal.species = "Dog"
animal.age = 7
animal.weight = 25
print(animal.species)
print(animal.age) 
print(animal.weight) 