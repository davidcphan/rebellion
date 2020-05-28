import argparse

# Global Constants
# =============================================================================
# Number of iterations for which the model runs
TURNS = None
# Percentage of board that is cops
INITIAL_COP_DENSITY = None
# Percentage of board that is agents
INITIAL_AGENT_DENSITY = None
# Number of grid positions in north/south/east/west directions that a 
# agent/cop can see
VISION = None
# A value between 0-1
GOVERNMENT_LEGITIMACY = None
# Maximmum umber of turns an agent will be jaled
MAX_JAIL_TURNS = None
# Whether agents and cops should move
MOVEMENT = None
# Enable extension 1 - whether an agent's hardship is affected 
# by the average hardship of agents in their vision
AVERAGE_HARDSHIP = None
# Enable extension 2 - whether cops can also behave like agents
ACTIVE_COPS = None
# Height of the grid
HEIGHT = None
# Width of the grid
WIDTH = None
# Turns on graphical simulation
SIMULATE = None

# An enum class for the color of a turtle
class Color():
    RED = 1
    GREEN = 2
    BLACK = 3
    CYAN = 4

# An enum class for a turtle type
class Type():
    AGENT = 1
    COP = 2

def initGlobals():
    # parge command line flags
    parser = argparse.ArgumentParser(
        description='Rebellion model parameters',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--turns', dest='turns', 
        action='store', type=int, default=10,
        help="Number of iterations for which the model runs")
    parser.add_argument('--initial-cop-density', dest='cop_density',
        action='store', type=float, default=0.04,
        help="Percentage of board that is cops")
    parser.add_argument('--initial-agent-density', 
        dest='agent_density', action='store', type=float, default=0.7,
        help="Percentage of board that is agents")
    parser.add_argument('--vision', dest='vision', 
        action='store', type=int, default=7,
        help="Number of grid positions in north/south/east/west  \
        directions that a agent/cop can see")
    parser.add_argument('--government-legitimacy', 
        dest='government_legitimacy', action='store', type=float, default=0.82)
    parser.add_argument('--max-jail-turns', 
        dest="max_jail_turns", action='store', type=int, default=30)
    parser.add_argument('--no-movement', 
        dest='movement', action='store_false',
        help="Stops agents and cops from moving")
    parser.add_argument('--active-cops', 
        dest='active_cops', action='store_true',
        help="Enable extension 2 - whether cops can \
            also behave like agents")
    parser.add_argument('--average-hardship', 
        dest='average_hardship', action='store_true',
        help="Enable extension 1 - whether an agent's \
        hardship is affected by the average hardship of agents in their \
        vision")
    parser.add_argument('--simulate',
        dest='simulate', action='store_true',
        help="Turns on graphical simulation")
    parser.add_argument('--width', 
        dest="width", action='store', type=int, default=40,
        help="Width of the grid")
    parser.add_argument('--height', 
        dest="height", action='store', type=int, default=20,
        help="Height of the grid")
    parser.set_defaults(movement=True, average_hardship=False,
        active_cops=False, simulate=False)
    args = parser.parse_args()

    # set global constants of our model from the arguments parsed from the 
    # command line
    global INITIAL_COP_DENSITY, INITIAL_AGENT_DENSITY, VISION, \
        GOVERNMENT_LEGITIMACY, MAX_JAIL_TURNS, TURNS, MOVEMENT, \
        AVERAGE_HARDSHIP, ACTIVE_COPS, SIMULATE, WIDTH, HEIGHT
    INITIAL_COP_DENSITY = args.cop_density
    INITIAL_AGENT_DENSITY = args.agent_density
    VISION = args.vision
    GOVERNMENT_LEGITIMACY = args.government_legitimacy
    MAX_JAIL_TURNS = args.max_jail_turns
    TURNS = args.turns
    MOVEMENT = args.movement
    AVERAGE_HARDSHIP = args.average_hardship
    ACTIVE_COPS = args.active_cops
    SIMULATE = args.simulate
    WIDTH = args.width
    HEIGHT = args.height
    