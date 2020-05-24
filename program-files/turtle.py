import abc

class Turtle(metaclass=abc.ABCMeta):
    def __init__(self, x, y):
        self.setPos(x, y)

    @abc.abstractmethod
    def update(self, grid):
        pass

    def getPos(self):
        return self.pos

    def setPos(self, x, y):
        self.pos = (x, y)

    def move(self, grid):
        grid.randomlyMoveTurtle(self)