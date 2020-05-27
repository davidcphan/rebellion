from turtle import Turtle
from agent import Agent
import config as cfg

class Cop(Turtle):
    
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self, grid):
        if cfg.MOVEMENT:
            self.move(grid)
        self.enforce(grid)

    def enforce(self, grid):
        grid.arrestAgent(self)

    def color(self):
        return cfg.Color.CYAN
    
    def getType(self):
        return cfg.Type.COP

    def __repr__(self):
        return "C"