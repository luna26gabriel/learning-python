class Animal:

    alive = True

    def sleep(slef):
        print("This animal is sleeping")

    def eat(self):
        print("This animal is Eating")

class Dog(Animal):
    
    def run(self):
        print("This dog is runnig")

    def eat(self): #This method is overwriting the above method
        print("This dog is Eating")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

dog = Dog()
# fish = Fish()
# hawk = Hawk()

# print(dog.alive)
# fish.eat()
# hawk.sleep()

dog.eat()
# fish.swin()
# hawk.fly()
