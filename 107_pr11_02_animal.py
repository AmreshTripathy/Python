class Animals:
    animalType = 'Mammals'

class Pet(Animals):
    color = 'white'

class Dog(Pet):
    @staticmethod
    def bark():
        print ('Bow Bow!')

d = Dog()
d.bark()