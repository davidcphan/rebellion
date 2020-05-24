import argparse

COP_DENSITY = None
AGENT_DENSITY = None
VISION = None
GOVERNMENT_LEGITIMACY = None
MAX_JAIL_TERMS = None
HEIGHT = 10
WIDTH = 10

def initGlobals():
    # parge arguments
    parser = argparse.ArgumentParser(description='Rebellion model parameters')
    parser.add_argument('--initial-cop-density', dest='cop_density',
        action='store', type=float, default=0.2, help='percentage of board that is cops')
    parser.add_argument('--initial-agent-density', dest='agent_density',
        action='store', type=float, default=0.4, help='percentage of board that is agents')
    parser.add_argument('--vision', dest='vision',
        action='store', type=int, default=7, help='number of grid positions in north/south/east/west directions that a agent/cop can see')
    parser.add_argument('--government-legitimacy', dest='government_legitimacy',
        action='store', type=float, default=0.82, help= 'a value between 0-1')
    parser.add_argument('--max-jail-terms', dest="max_jail_terms",
        action='store', type=int, default=30, help='number of turns an agent will be jaled')
    args = parser.parse_args()

    # set globals
    global COP_DENSITY, AGENT_DENSITY, VISION, GOVERNMENT_LEGITIMACY, MAX_JAIL_TERMS
    COP_DENSITY = args.cop_density
    AGENT_DENSITY = args.agent_density
    VISION = args.vision
    GOVERNMENT_LEGITIMACY = args.government_legitimacy
    MAX_JAIL_TERMS = args.max_jail_terms