from turtle import Turtle
from agent import Agent
import config as cfg

class Cop(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self, grid):
        if cfg.ACTIVE_COPS:
            super().update(grid)
        else:
            self.move(grid)
        if not self.isActive() and not self.isJailed():
            self.enforce(grid)

    def enforce(self, grid):
        grid.arrestAgent(self)

    def color(self):
        if self.isActive():
            return cfg.Color.RED
        elif self.isJailed():
            return cfg.Color.BLACK
        else:
            return cfg.Color.CYAN
    
    def getType(self):
        return cfg.Type.COP

    def __repr__(self):
        return "C"