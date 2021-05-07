from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motocycle(Vehicle):

    def go(self):
        print("You ride the motocycle")

    def stop(self):
        print("You stop the motocycle")


car = Car()
moto = Motocycle()


car.go()
moto.go()

car.stop()
moto.stop()
