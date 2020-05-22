from grid import Grid

HEIGHT = 4
WIDTH = 4
NUM_AGENTS = 3
NUM_COPS = 3

def __main__():
    newGrid = Grid(HEIGHT, WIDTH)
    #Need to check if number of agents/cops exceed space on grid
    newGrid.populate(NUM_AGENTS, NUM_COPS)
    newGrid.printArr()


__main__()