from turtle import Turtle
from cop import Cop
from agent import Agent
import random

class Grid:
    def __init__(self, h, w, vision, agent_density, cop_density):
        self.h, self.w = h, w
        self.vision = vision
        # Initialise an empty 2D grid
        self.grid = [[None for col in range(0,w)] for row in range(0,h)]
        random.shuffle(self.empty_positions)

        num_agents = int(h * w * agent_density)
        num_cops = int(h * w * cop_density)

        # gets random cell that's empty
        empty_positions = [(row,col) for col in range(0,w) for row in range(0,h)]
        getEmptyCell = lambda: empty_positions.pop()

        # populate grid with Agents and Cops
        self.agents, self.cops = [], []
        for _ in range(0, num_agents):
            row, col = getEmptyCell()
            self.grid[row][col] = Agent(row, col)
            self.agents.append(self.grid[row][col])
        for cops in range(0, num_cops):
            row, col = getEmptyCell()
            self.grid[row][col] = Cop(row, col)
            self.cops.append(self.grid[row][col])

    def getTurtles(self):
        return self.agents, self.cops

    def getVisibleField(self, turtle):
        # search for vacant positions within vision field
        row, col = turtle.getPos()
        is_pos_vacant = lambda row, col: self.grid[row][col] == None
        v_rng = range(-self.vision, self.vision)
        vacant_poss = filter(is_pos_vacant,
            [(row+drow, col+dcol) for dcol in v_rng for drow in v_rng])
        return vacant_poss

    def randomlyMoveTurtle(self, turtle):
        vacant_poss = self.getVisibleField(turtle)
        # Choose random vacant position (if ant)
        if(len(vacant_poss) == 0):
            return
        i = random.uniform(0, len(vacant_poss)-1)
        nrow, ncol = vacant_poss[i]
        # move turtle
        turtle.setPos(nrow, ncol)
        self.grid[row][col] = None
        self.grid[nrow][ncol] = turtle

    def searchNeighbourhood(self, turtle):
        vacant_poss = self.getVisibleField(turtle)
        cops, active_agents = [], []
        for row, col in vacant_poss:
            turtle = self.grid[row][col]
            if isinstance(turtle, Cop):
                cops.append(turtle)
            elif isinstance(turtle, Agent) and turtle.isActive():
                active_agents.append(turtle)
        return active_agents, cops

    def arrestAgent(self, cop):
        active_agents, _ = self.searchNeighbourhood(cop)
        if(len(active_agents) == 0):
            return
        agent = active_agents[random.uniform(0, len(active_agents)-1)]
        agent.setJailed(True)
        agent.setActive(False)

    def printArr(self):
        for row in self.grid:
            print(str(row))
        print("\n")





        

    