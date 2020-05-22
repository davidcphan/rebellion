from turtle import Turtle
from cop import Cop
from agent import Agent

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

    
    def main(self):
        print(str(self.arr_turtle))


        

    