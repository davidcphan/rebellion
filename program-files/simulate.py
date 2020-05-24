from grid import Grid
import config as cfg
import curses
import time

def simulate(window):

    # Initialize grid
    grid = Grid()
    turtles = grid.initialize()

    for i in range(1, 10):
        for turtle in turtles:
            turtle.update(grid)

        window.addstr(0, 0, str(grid))
        window.refresh()
        time.sleep(0.5)
        

def __main__():
    cfg.initGlobals()
    if cfg.COP_DENSITY + cfg.AGENT_DENSITY > 1:
        raise Exception("sum of agent and cop densities should not be greater than 100")

    # Call simulation
    curses.wrapper(simulate)


__main__()