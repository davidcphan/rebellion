class Turtle:

    def __init__(self, row, col, grid):
        self.row = row
        self.col = col
        self.grid = grid

    def move(self):
        self.grid.move_turtle(self)


        