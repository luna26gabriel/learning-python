class Eletronic:

    socket = 1

    def __init__(self, model, yaer, size, typ):
        self.model = model
        self.yaer = yaer
        self.size = size
        self.typ = typ

    def trunOn(self):
        print("Now " + self.model + " is on")

    def trunOff(self):
        print("Now " + self.model + " is off")

    


