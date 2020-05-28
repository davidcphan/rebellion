import argparse

# Global Constants
# =======================================================================================
# Percentage of board that is cops
INITIAL_COP_DENSITY = None
# Percentage of board that is agents
INITIAL_AGENT_DENSITY = None
# Number of grid positions in north/south/east/west directions that a agent/cop can see
VISION = None
# A value between 0-1
GOVERNMENT_LEGITIMACY = None
# Maximmum umber of turns an agent will be jaled
MAX_JAIL_TURNS = None
# Whether agents and cops should use the movement update rule
MOVEMENT = None
# A boolean to enable extension 1 - whether an agent's hardship is affected by the
# average hardship of agents in their vision
AVERAGE_HARDSHIP = None
# A boolean to enable extension 2 - whether cops can also behave like agents
ACTIVE_COPS = None
# Height of the grid
HEIGHT = 20
# Width of the grid
WIDTH = 60
# Number of turns for which the model will run
TURNS = 10

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
    parser = argparse.ArgumentParser(description='Rebellion model parameters')
    parser.add_argument('--turns', dest='turns', action='store', type=int, default=10)
    parser.add_argument('--initial-cop-density', dest='cop_density', action='store', type=float, default=0.04)
    parser.add_argument('--initial-agent-density', dest='agent_density', action='store', type=float, default=0.7)
    parser.add_argument('--vision', dest='vision', action='store', type=int, default=7)
    parser.add_argument('--government-legitimacy', dest='government_legitimacy', action='store', type=float, default=0.82)
    parser.add_argument('--max-jail-turns', dest="max_jail_turns", action='store', type=int, default=30)
    parser.add_argument('--no-movement', dest='movement', action='store_false')
    parser.add_argument('--active-cops', dest='active_cops', action='store_true')
    parser.add_argument('--average-hardship', dest='average_hardship', action='store_true')
    parser.set_defaults(movement=True, average_hardship=False, active_cops=False)
    args = parser.parse_args()

    # set global constants of our model from the arguments parsed from the command line
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
    