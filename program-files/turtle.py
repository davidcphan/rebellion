class Turtle:

    def __init__(self, x, y):
        self.setPos(x, y)

    def getPos(self):
        return self.pos

    def setPos(self, x, y):
        self.pos = (x, y)

    def move(self, grid):
        grid.randomlyMoveTurtle(self)