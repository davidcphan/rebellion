from grid import Grid
import config as cfg
import curses
import time


# agents are green - normal, red - active, black - jailed
# cops are blue
def simulate(window):

    # Agent = normal - green, active - red, jailed - black
    # Cops = cyan
    curses.init_pair(cfg.Color.RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(cfg.Color.GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(cfg.Color.BLACK, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(cfg.Color.CYAN, curses.COLOR_CYAN, curses.COLOR_BLACK)

    # Initialize grid
    grid = Grid()
    turtles = grid.initialize()

    while True:
        for turtle in turtles:
            turtle.update(grid)

        window.clear()
        for turtle in turtles:
            y, x = turtle.getPos()
            color = turtle.color()
            window.addstr(y, x, str(turtle), curses.color_pair(color))
        window.refresh()
        time.sleep(0.1)
        

def __main__():
    cfg.initGlobals()
    if cfg.COP_DENSITY + cfg.AGENT_DENSITY > 1:
        raise Exception("sum of agent and cop densities should not be greater than 100")

    # Call simulation
    curses.wrapper(simulate)
    # simulate(None)
    


__main__()