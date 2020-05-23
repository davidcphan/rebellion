from turtle import Turtle

class Cop(Turtle):
    
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "Cop"