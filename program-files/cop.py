from turtle import Turtle

class Cop(Turtle):
    def run(self):
        #make arrent or move
        self.move()

    #represents opbject as a string called Cop when printed
    def __repr__(self):
        return "Cop"