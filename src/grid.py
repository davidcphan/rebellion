from cop import Cop
from agent import Agent
import config as cfg
import random

class Grid:
    def __init__(self):
        self.grid = [[None for col in range(0, cfg.WIDTH)]
                            for row in range(0, cfg.HEIGHT)]

    def initialize(self):
        # Initialise an empty 2D grid
        num_agents = int(cfg.HEIGHT * cfg.WIDTH * cfg.INITIAL_AGENT_DENSITY)
        num_cops = int(cfg.HEIGHT * cfg.WIDTH * cfg.INITIAL_COP_DENSITY)

        # gets random cell that's empty
        empty_positions = [(row,col) for col in range(0, cfg.WIDTH)
                                        for row in range(0, cfg.HEIGHT)]
        random.shuffle(empty_positions)
        getEmptyCell = lambda: empty_positions.pop()

        # populate grid with Agents and Cops
        turtles = []
        for i in range(0, num_agents + num_cops):
            row, col = getEmptyCell()
            turtle = Agent(row, col) if i < num_agents else Cop(row, col)
            self.grid[row][col] = turtle
            turtles.append(turtle)
        return turtles

    def getVisibleField(self, turtle):
        # search for vacant positions within vision field
        row, col = turtle.getPos()
        v_rng = range(-cfg.VISION, cfg.VISION)
        visible_field = []
        for drow in v_rng:
            for dcol in v_rng:
                nrow, ncol = row + drow, col + dcol
                if nrow >= 0 and nrow < cfg.HEIGHT and ncol >= 0 and ncol < cfg.WIDTH:
                    visible_field.append((nrow, ncol))
        return visible_field

    def randomlyMoveTurtle(self, turtle):
        # Filter vacant positions in visible field
        visible_field = self.getVisibleField(turtle)
        is_pos_vacant = lambda pos: self.grid[pos[0]][pos[1]] == None
        vacant_positions = list(filter(is_pos_vacant, visible_field))
        # Choose random vacant position (if any)
        if(len(vacant_positions) == 0):
            return
        i = random.randint(0, len(vacant_positions)-1)
        nrow, ncol = vacant_positions[i]
        # move turtle
        row, col = turtle.getPos()
        turtle.setPos(nrow, ncol)
        self.grid[row][col] = None
        self.grid[nrow][ncol] = turtle

    def searchNeighbourhood(self, turtle):
        visible_field = self.getVisibleField(turtle)
        active, neutral, cops = [], [], []
        for row, col in visible_field:
            turtle = self.grid[row][col]
            if isinstance(turtle, Cop):
                cops.append(turtle)
            elif isinstance(turtle, Agent):
                if turtle.isActive():
                    active.append(turtle)
                else:
                    neutral.append(turtle)
        return active, neutral, cops

    def arrestAgent(self, cop):
        active, _, _ = self.searchNeighbourhood(cop)
        if(len(active) == 0):
            return
        i = random.randint(0, len(active)-1)
        random_active_agent = active[i]
        jail_turns = random.randint(0, cfg.MAX_JAIL_TURNS)
        random_active_agent.setJailed(jail_turns)

    def __str__(self):
        grid = ""
        for row in self.grid:
            grid += str(row)
            grid += "\n"
        return grid





        

    