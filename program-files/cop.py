from turtle import Turtle

class Cop(Turtle):
    
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self, grid):
        self.move(grid)
        self.enforce(grid)

    def enforce(self, grid):
        grid.arrestAgent(self)

    def __repr__(self):
        return "Cop"