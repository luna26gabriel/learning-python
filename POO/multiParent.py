class Prey:
    def flee(self):
        print("This animals is flees")

class Predator:
    def hunt(self):
        print("This animals is hunting")


class Rabit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabit = Rabit()
hawk = Hawk()
fish = Fish()

# rabit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()