from grid import Grid

HEIGHT = 4
WIDTH = 4
NUM_AGENTS = 2
NUM_COPS = 2
TURNS = 2
VISION = 1

def __main__():
    newGrid = Grid(HEIGHT, WIDTH)
    #Need to check if number of agents/cops exceed space on grid
    newGrid.populate(NUM_AGENTS, NUM_COPS)
    newGrid.printArr()
    newGrid.run(TURNS)

__main__()