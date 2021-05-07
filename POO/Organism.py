class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("this animal is eating")

class Dog(Animal):

    def run(self):
        print("this dog is runnig")


dog = Dog()

print(dog.alive)
dog.eat()
dog.run()