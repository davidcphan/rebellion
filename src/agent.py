from turtle import Turtle
import config as cfg
import random
import functools as f
import math

# Represents an agent
class Agent(Turtle):

    # Initialises all parameters of an agent
    def __init__(self, x, y):
        super().__init__(x, y)
        # Agents are initially neutral
        self.active = False
        self.jailed_turns = 0
        # Initialises local parameters uniformly at random
        self.percieved_harship = random.uniform(0, 1)
        self.risk_aversion = random.uniform(0, 1)
        # set such that the probability of rebelling is approximately 0.9 when C = 1 and A = 1
        self.k = 2.3
        # real number in [0,1]
        self.threshold = 0.1

    # Updates an agents state according to
    # Movement rule B: Move to a random site within your vision
    # Agent rule A: If grievence - net risk > threshold be active; else neutral
    def update(self, grid):
        # If an agent is jailed it cannot move
        if not self.isJailed() and cfg.MOVEMENT:
            self.move(grid)
            self.determineBehaviour(grid)
        else:
            self.jailed_turns = self.jailed_turns - 1

    # Calculates grievence as a function of percieved hardship and government legitimacy
    def calculateGrievence(self, agents):
        hardship = self.percieved_harship
        # An agents hardship if affected by the hardship of other agents
        if cfg.AVERAGE_HARDSHIP:
            av_hardship = f.reduce(lambda acc, agent: agent.percieved_harship + acc, agents, 0) / len(agents)
            hardship = (hardship + av_hardship) / 2
        return hardship * (1 - cfg.GOVERNMENT_LEGITIMACY)

    # Calculates net risk as a function of an agent's risk averseness and the probability
    # of arrest.
    def calculateNetRisk(self, num_actives, num_cops):
        # Avoid divide by zero by counting yourself as active agent
        num_actives = num_actives + 1
        # Take the floor of (active agents / cops) as the netlogo model perscribes
        arrest_probability = 1 - math.exp(-self.k * math.floor(num_cops / num_actives))
        return self.risk_aversion * arrest_probability

    # Updates the agents 'active' state according to
    # Agent rule A: If grievence - net risk > threshold be active; else neutral
    def determineBehaviour(self, grid):
        active, neutral, cops = grid.searchNeighbourhood(self)
        self.active = self.calculateGrievence(active+neutral) -  \
            self.calculateNetRisk(len(active), len(cops)) > self.threshold
    
    # Jail an agent for some number of turns
    def setJailed(self, turns):
        self.jailed_turns = turns
        if self.jailed_turns > 0:
            self.active = False

    # Returns whether an agent is active
    def isActive(self):
        return self.active

    # Returns whether an agent is jailed
    def isJailed(self):
        return self.jailed_turns > 0

    # Returns turtle type
    def getType(self):
        return cfg.Type.AGENT

    # Color of agent
    def color(self):
        if self.isActive():
            return cfg.Color.RED
        elif self.isJailed():
            return cfg.Color.BLACK
        else:
            return cfg.Color.GREEN

    # String representation of agent
    def __repr__(self):
        return "A"