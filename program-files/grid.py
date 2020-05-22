from turtle import Turtle
from cop import Cop
from agent import Agent
import random

class Grid:

    def __init__(self, H, W):
        self.grid = []
        self.turtles = []
        self.H = H
        self.W = W

        #initialise table with None values
        for i in range(0, H):
            init_row = []
            for j in range(0, W):
                init_row.append(None)
            self.grid.append(init_row)

    #function will execute run method for every turtle in random order
    #turns is how many times you want to run the simulation
    def run(self, turns):
        #generate list, that will be used to process list in random order
        rand_lst = self.rand_list(len(self.turtles))
        for turn in range(0, turns):
            print("-----"+"Turn: "+str(turn+1)+"-----")
            for index in rand_lst:
                self.turtles[index].run()    

    #populate grid with turtles randomly
    def populate(self, Agents, Cops):
        #populate grid with Agents
        for agent in range(0, Agents):
            emptyCell = self.getEmptyCell()
            row = emptyCell[0]
            col = emptyCell[1]
            agent = Agent(row, col, self)
            self.grid[row][col] = agent
            self.turtles.append(agent)
        #populate grid with cops
        for cops in range(0, Cops):
            emptyCell = self.getEmptyCell()
            row = emptyCell[0]
            col = emptyCell[1]
            cop = Cop(row, col, self)
            self.grid[row][col] = cop
            self.turtles.append(cop)
        print("-----"+"Intial state"+"-----")


    #gets random cell that's empty
    def getEmptyCell(self):
        x = random.sample(range(0, self.W), self.W)
        y = random.sample(range(0, self.H), self.H)
        for row in y:
            for col in x:
                if(not self.grid[row][col]):
                    #cell is empty return co-ordinate
                    return (row, col)
    
    #moves a turtle
    def move_turtle(self, turtle):
        #remember to change vision to vision variable
        adj_cells = self.get_adjacent_cells(turtle.row, turtle.col, 1)
        for cell in adj_cells:
            row = cell[0]
            col = cell[1]
            if(not self.grid[row][col]):
                #if cell is empty then swap
                self.grid[turtle.row][turtle.col], self.grid[row][col] = self.grid[row][col], self.grid[turtle.row][turtle.col]
                #update rows and cols
                turtle.col = col
                turtle.row = row
            
        self.printArr()

    #random number list generator 
    #used to generate list of unique range of random numbers of specific length
    def rand_list(self, MAX_VALUE):
        lst = random.sample(range(0, MAX_VALUE), MAX_VALUE)
        return lst


    #get empty cell adjacent that turtle can move to
    def get_adjacent_cells(self, row, col, vision):
        #list stores adjacent cells as tuples eg.[(1,2), (2,2)]
        adj_cells = []
        for r in range(-vision, vision+1):
            row_value = row + r
            #if row value is out of bounds continue
            if(row_value<0 or row_value>=self.H):
                continue
            else:
                for c in range(-vision, vision+1):
                    col_value = col + c
                    #if col vlaue is out of bounds continue
                    if(col_value<0 or col_value>=self.W):
                        continue
                    #do not count current row
                    elif(r == c == 0):
                        continue
                    else:
                        adj_cells.append((row_value, col_value))
        #print(adj_cells)
        return adj_cells


    #prints array for inspection
    def printArr(self):
        for row in self.grid:
            print(str(row))
        print("\n")





        

    