import argparse

INITIAL_COP_DENSITY = None
INITIAL_AGENT_DENSITY = None
VISION = None
GOVERNMENT_LEGITIMACY = None
MAX_JAIL_TURNS = None
MOVEMENT = None
AVERAGE_HARDSHIP = None
ACTIVE_COPS = None
HEIGHT = 20
WIDTH = 60
TURNS = 10

class Color():
    RED = 1
    GREEN = 2
    BLACK = 3
    CYAN = 4

class Type():
    AGENT = 1
    COP = 2

def initGlobals():
    # parge arguments
    parser = argparse.ArgumentParser(description='Rebellion model parameters')
    parser.add_argument('--turns', dest='turns',
        action='store', type=int, default=10, help='number of simulaton turns')
    parser.add_argument('--initial-cop-density', dest='cop_density',
        action='store', type=float, default=0.04, help='percentage of board that is cops')
    parser.add_argument('--initial-agent-density', dest='agent_density',
        action='store', type=float, default=0.7, help='percentage of board that is agents')
    parser.add_argument('--vision', dest='vision',
        action='store', type=int, default=7, help='number of grid positions in north/south/east/west directions that a agent/cop can see')
    parser.add_argument('--government-legitimacy', dest='government_legitimacy',
        action='store', type=float, default=0.82, help= 'a value between 0-1')
    parser.add_argument('--max-jail-turns', dest="max_jail_turns",
        action='store', type=int, default=30, help='number of turns an agent will be jaled')
    parser.add_argument('--no-movement', dest='movement', action='store_false')
    parser.add_argument('--active-cops', dest='active_cops', action='store_true')
    parser.add_argument('--average-hardship', dest='average_hardship', action='store_true')
    parser.set_defaults(movement=True, average_hardship=False, active_cops=False)
    args = parser.parse_args()

    # set globals
    global INITIAL_COP_DENSITY, INITIAL_AGENT_DENSITY, VISION, GOVERNMENT_LEGITIMACY, MAX_JAIL_TURNS, TURNS, MOVEMENT, AVERAGE_HARDSHIP, ACTIVE_COPS
    INITIAL_COP_DENSITY = args.cop_density
    INITIAL_AGENT_DENSITY = args.agent_density
    VISION = args.vision
    GOVERNMENT_LEGITIMACY = args.government_legitimacy
    MAX_JAIL_TURNS = args.max_jail_turns
    TURNS = args.turns
    MOVEMENT = args.movement
    AVERAGE_HARDSHIP = args.average_hardship
    ACTIVE_COPS = args.active_cops
    