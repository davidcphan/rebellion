from turtle import Turtle

class Agent(Turtle):

    def __init__(self, x, y):
        self.active = False
        super().__init__(x, y)

    def isActive(self):
        return self.active

    def setActive(self, active):
        self.active = active

    def isJailed(self):
        return self.jailed
    
    def setJailed(self, jailed):
        self.jailed = jailed

    def __repr__(self):
        return "Agent"