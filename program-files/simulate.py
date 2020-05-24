from grid import Grid
import argparse
import curses
import time

HEIGHT, WIDTH = 20, 20

def simulate(window, args):
    grid = Grid(HEIGHT, WIDTH, args.vision)
    agents, cops = grid.initialize(args.initial_agent_density, args.initial_cop_density)
    for i in range(1, 10):
        window.addstr(0, 0, str(grid))
        window.refresh()
        time.sleep(0.5)
        for turtle in agents + cops:
            turtle.move(grid)
        

def __main__():
    # parge arguments
    parser = argparse.ArgumentParser(description='Rebellion model parameters')
    parser.add_argument('--initial-cop-density', dest='initial_cop_density',
        action='store', type=float, default=0.2, help='percentage of board that is cops')
    parser.add_argument('--initial-agent-density', dest='initial_agent_density',
        action='store', type=float, default=0.4, help='percentage of board that is agents')
    parser.add_argument('--vision', dest='vision',
        action='store', type=int, default=7, help='number of grid positions in north/south/east/west directions that a agent/cop can see')
    parser.add_argument('--activation-threshold', dest='activation_threshold',
        action='store', type=float, default=0.1, help='the threshold for Grievence - Percieved Risk after which an agent goes active')
    parser.add_argument('--government-legitimacy', dest='government-legitimacy',
        action='store', type=float, default=0.82, help= 'a value between 0-1')
    parser.add_argument('--max-jail-terms', dest="max_jail_terms",
        action='store', type=int, default=30, help='number of turns an agent will be jaled')
    args = parser.parse_args()

    # Call simulation
    curses.wrapper(simulate, args)

    # grid = Grid(HEIGHT, WIDTH, args.vision)
    # agents, cops = grid.initialize(args.initial_agent_density, args.initial_cop_density)
    # print(grid)

__main__()