import abc

# A turtle represents an entity on the grid. There are two types of turtles, cops and agents.
# This abstract base class keeps all logic common to cops and agents (e.g. movement) 
class Turtle(metaclass=abc.ABCMeta):
    def __init__(self, y, x):
        self.setPos(y, x)

    # Updates an turtle's state according to their unique rule set
    @abc.abstractmethod
    def update(self, grid):
        pass

    # Returns an turtle's color based on state (active, jailed, neutral)
    @abc.abstractmethod
    def color(self):
        pass

    # Returns an turtle's type (cop, agent)
    @abc.abstractmethod
    def getType(self):
        pass

    # Return position of turtle on grid
    def getPos(self):
        return self.pos

    # Set position of turtle on grid
    def setPos(self, y, x):
        self.pos = (y, x)

    # Move the turtle to some random position within their field of vision
    def move(self, grid):
        grid.randomlyMoveTurtle(self)