class Ball:

    def __init__(self, canvas, x, y, diameter, xSpeed, ySpeed, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed

    def move(self):
        coordinates = self.canvas.coords(self.image)
        if(coordinates[2] >= (self.canvas.winfo_width()) or coordinates[0] < 0):
            self.xSpeed = -self.xSpeed
        if(coordinates[3] >= (self.canvas.winfo_height()) or coordinates[1] < 0):
            self.ySpeed = -self.ySpeed
        self.canvas.move(self.image, self.xSpeed, self.ySpeed)

