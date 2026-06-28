class Animal:
    def__init__(self, name, habitat):
       self.name = name
       self.habitat =  habitat
    
class Dog(Animal):
    def__init__(self, nmae, habitat, breed):
       Animal.__init__(self, name, habitat)
       self.breed = breed
    
d = Dog("Bruno", "Home", "Labrador")
print(d.name)
print(d.breed)
    
