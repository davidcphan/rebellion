from turtle import Turtle
from cop import Cop
from agent import Agent
import random

class Grid:
    def __init__(self, h, w, vision):
        self.h, self.w = h, w
        self.vision = vision
        self.grid = [[None for col in range(0,w)] for row in range(0,h)]

    def initialize(self, agent_density, cop_density):
        # Initialise an empty 2D grid
        num_agents = int(self.h * self.w * agent_density)
        num_cops = int(self.h * self.w * cop_density)

        # gets random cell that's empty
        empty_positions = [(row,col) for col in range(0,self.w) for row in range(0,self.h)]
        random.shuffle(empty_positions)
        getEmptyCell = lambda: empty_positions.pop()

        # populate grid with Agents and Cops
        agents, cops = [], []
        for _ in range(0, num_agents):
            row, col = getEmptyCell()
            self.grid[row][col] = Agent(row, col)
            agents.append(self.grid[row][col])
        for _ in range(0, num_cops):
            row, col = getEmptyCell()
            self.grid[row][col] = Cop(row, col)
            cops.append(self.grid[row][col])
        return agents, cops

    def getVisibleField(self, row, col):
        # search for vacant positions within vision field
        v_rng = range(-self.vision, self.vision)
        visible_field = []
        for drow in v_rng:
            for dcol in v_rng:
                nrow, ncol = row + drow, col + dcol
                if nrow >= 0 and nrow < self.h and ncol >= 0 and ncol < self.w:
                    visible_field.append((nrow, ncol))
        return visible_field

    def randomlyMoveTurtle(self, turtle):
        # Filter vacant positions in visible field
        row, col = turtle.getPos()
        visible_field = self.getVisibleField(row, col)
        # vacant_positions = [(row, col) if ]
        is_pos_vacant = lambda pos: self.grid[pos[0]][pos[1]] == None
        vacant_positions = list(filter(is_pos_vacant, visible_field))
        # Choose random vacant position (if ant)
        if(len(vacant_positions) == 0):
            return
        i = random.randint(0, len(vacant_positions)-1)
        nrow, ncol = vacant_positions[i]
        # move turtle
        turtle.setPos(nrow, ncol)
        self.grid[row][col] = None
        self.grid[nrow][ncol] = turtle

    def searchNeighbourhood(self, turtle):
        visible_field = self.getVisibleField(turtle)
        active_agents, cops = [], []
        for row, col in visible_field:
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
        i = random.randint(0, len(active_agents)-1)
        random_active_agent = active_agents[i]
        random_active_agent.setJailed(True)
        random_active_agent.setActive(False)

    def __str__(self):
        grid = ""
        for row in self.grid:
            grid += str(row)
            grid += "\n"
        return grid





        

    