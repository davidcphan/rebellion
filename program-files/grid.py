from turtle import Turtle
from cop import Cop
from agent import Agent
import random

class Grid:

    def __init__(self, H, W):
        self.arr_turtle = []
        self.H = H
        self.W = W

        #initialise table with None values
        for i in range(0, H):
            init_row = []
            for j in range(0, W):
                init_row.append(None)
            self.arr_turtle.append(init_row)

    #populate grid with turtles randomly
    def populate(self, Agents, Cops):
        #populate grid with Agents
        for agent in range(0, Agents):
            emptyCell = self.getEmptyCell()
            row = emptyCell[0]
            col = emptyCell[1]
            self.arr_turtle[row][col] = Agent()
        #populate grid with cops
        for cops in range(0, Cops):
            emptyCell = self.getEmptyCell()
            row = emptyCell[0]
            col = emptyCell[1]
            self.arr_turtle[row][col] = Cop()



    #gets random cell that's empty
    def getEmptyCell(self):
        x = random.sample(range(0, self.W), self.W)
        y = random.sample(range(0, self.H), self.H)
        for row in y:
            for col in x:
                if(not self.arr_turtle[row][col]):
                    #cell is empty return co-ordinate
                    return (row, col)

    #prints array for inspection
    def printArr(self):
        for row in self.arr_turtle:
            print(str(row))





        

    