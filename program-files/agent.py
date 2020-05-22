from turtle import Turtle

class Agent(Turtle):
    
    def run(self):
        #calculate arrest probability
        #rebel or move
        self.grid.move_turtle(self)

    #represents opbject as a string called Agent when printed
    def __repr__(self):
        return "Agent"