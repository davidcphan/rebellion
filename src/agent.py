from turtle import Turtle
import config as cfg
import random
import functools as f
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
            if cfg.MOVEMENT:
                self.move(grid)
            self.determineBehaviour(grid)
        else:
            self.jailed_turns = self.jailed_turns - 1


    def calculateGrievence(self, agents):
        hardship = self.percieved_harship
        if cfg.AVERAGE_HARDSHIP:
            av_hardship = f.reduce(lambda acc, agent: agent.percieved_harship + acc, agents, 0) / len(agents)
            hardship = (hardship + av_hardship) / 2
        return hardship * (1 - cfg.GOVERNMENT_LEGITIMACY)

    def calculateNetRisk(self, num_actives, num_cops):
        # Avoid divide by zero by counting yourself as active agent
        num_actives = num_actives + 1
        arrest_probability = 1 - math.exp(-self.k * math.floor(num_cops / num_actives))
        return self.risk_aversion * arrest_probability

    def determineBehaviour(self, grid):
        active, neutral, cops = grid.searchNeighbourhood(self)
        self.active = self.calculateGrievence(active+neutral) -  \
            self.calculateNetRisk(len(active), len(cops)) > self.threshold
    
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