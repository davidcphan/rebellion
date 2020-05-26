from turtle import Turtle
import config as cfg
import random
import math

class Agent(Turtle):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.active = False
        self.jailed_turns = 0
        self.percieved_harship = random.uniform(0, 1)
        self.risk_aversion = random.uniform(0, 1)
        # set s.t. probability of rebelling is approximately 0.9 when C = 1 and A = 1
        self.k = 2.3
        # real number in [0,1]
        self.threshold = 0.1

    def update(self, grid):
        if not self.isJailed():
            self.move(grid)
            self.determineBehaviour(grid)
        else:
            self.jailed_turns = self.jailed_turns - 1


    def calculateGrievence(self):
        return self.percieved_harship * (1 - cfg.GOVERNMENT_LEGITIMACY)

    def calculateNetRisk(self, grid):
        active_agents, cops = grid.searchNeighbourhood(self)
        # Avoid divide by zero by counting yourself as active agent
        A, C = len(active_agents) + 1, len(cops)
        arrest_probability = 1 - math.exp(-self.k * math.floor(C / A))
        return self.risk_aversion * arrest_probability

    def determineBehaviour(self, grid):
        self.active = self.calculateGrievence() - self.calculateNetRisk(grid) > self.threshold
    
    def setJailed(self, turns):
        self.jailed_turns = turns
        if self.jailed_turns > 0:
            self.active = False

    def isActive(self):
        return self.active

    def isJailed(self):
        return self.jailed_turns > 0

    def getType(self):
        return cfg.Type.AGENT

    def color(self):
        if self.isActive():
            return cfg.Color.RED
        elif self.isJailed():
            return cfg.Color.BLACK
        else:
            return cfg.Color.GREEN

    def __repr__(self):
        return "A"