from turtle import Turtle
from agent import Agent
import config as cfg

# Represents a cop
# As per our second extension, our cop can additionally behave as an agent.
class Cop(Agent):
    # Initialises all parameters of a cop
    def __init__(self, x, y):
        # Initialises all agent and turtle parameters
        super().__init__(x, y)

    # If we aren't using the --active-cops flag. A cop updates its state according to
    # Movement rule B: Move to a random site within your vision
    # Cop rule C: Inspect all sites within vision radius and arrest a random active agent.
    # As prescribed by the base model. Otherwise it additionally uses update rule
    # Agent rule A: If grievence - net risk > threshold be active; else neutral
    def update(self, grid):
        if cfg.ACTIVE_COPS:
            super().update(grid)
        else:
            self.move(grid)
        if not self.isActive() and not self.isJailed():
            self.enforce(grid)

    # Arrests a random active agent (if any) within the cop's vision radius
    def enforce(self, grid):
        grid.arrestAgent(self)

    # Returns color of cop
    def color(self):
        if self.isActive():
            return cfg.Color.RED
        elif self.isJailed():
            return cfg.Color.BLACK
        else:
            return cfg.Color.CYAN
    
    # Returns type of turtle - Cop
    def getType(self):
        return cfg.Type.COP

    # String representation of Cop
    def __repr__(self):
        return "C"