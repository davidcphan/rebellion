from grid import Grid
import argparse

HEIGHT, WIDTH = 4, 4

def __main__():
    # parge arguments
    parser = argparse.ArgumentParser(description='Rebellion model parameters')
    parser.add_argument('--initial-cop-density', dest='initial_cop_density',
        action='store', type=float, default=0.04, help='percentage of board that is cops')
    parser.add_argument('--initial-agent-density', dest='initial_agent_density',
        action='store', type=float, default=0.7, help='percentage of board that is agents')
    parser.add_argument('--vision', dest='vision',
        action='store', type=int, default=7, help='number of grid positions in north/south/east/west directions that a agent/cop can see')
    parser.add_argument('--activation-threshold', dest='activation_threshold',
        action='store', type=float, default=0.1, help='the threshold for Grievence - Percieved Risk after which an agent goes active')
    parser.add_argument('--government-legitimacy', dest='government-legitimacy',
        action='store', type=float, default=0.82, help= 'a value between 0-1')
    parser.add_argument('--max-jail-terms', dest="max_jail_terms",
        action='store', type=int, default=30, help='number of turns an agent will be jaled')
    args = parser.parse_args()

    grid = Grid(HEIGHT, WIDTH, args.initial_agent_density, args.initial_cop_density)
    # Need to check if number of agents/cops exceed space on grid
    # newGrid.populate(NUM_AGENTS, NUM_COPS)
    grid.printArr()

    agents, cops = grid.getTurtles()
    while True:
        for turtle in agents + cops:
            turtle.move(grid)
        

__main__()