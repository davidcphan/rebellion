from grid import Grid

HEIGHT = 2
WIDTH = 2
NUM_AGENTS = 1
NUM_COPS = 1

def __main__():
    newGrid = Grid(HEIGHT, WIDTH)
    #Need to check if number of agents/cops exceed space on grid
    newGrid.populate(NUM_AGENTS, NUM_COPS)
    newGrid.printArr()
    newGrid.getEmptyCell()


__main__()