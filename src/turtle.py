import abc

class Turtle(metaclass=abc.ABCMeta):
    def __init__(self, y, x):
        self.setPos(y, x)

    @abc.abstractmethod
    def update(self, grid):
        pass

    @abc.abstractmethod
    def color(self):
        pass

    @abc.abstractmethod
    def getType(self):
        pass

    def getPos(self):
        return self.pos

    def setPos(self, y, x):
        self.pos = (y, x)

    def move(self, grid):
        grid.randomlyMoveTurtle(self)