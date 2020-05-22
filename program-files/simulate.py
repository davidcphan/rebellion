from grid import Grid

HEIGHT = 2
WIDTH = 2
AGENTS = 1
COPS = 1

def __main__():
    newGrid = Grid(HEIGHT, WIDTH)
    newGrid.populate()
    newGrid.printArr()


__main__()