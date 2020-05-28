from grid import Grid
import config as cfg
import sys
import curses
import time
import csv


# Draws a simulation of the model onto a colorized terminal
def simulate(window):

    # Create foreground/background color pairs
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
        # Update state of turtles accroding to movement rules
        for turtle in turtles:
            turtle.update(grid)

        # Draws the turtles onto the terminal
        window.clear()
        for turtle in turtles:
            y, x = turtle.getPos()
            color = turtle.color()
            window.addstr(y, x, str(turtle), curses.color_pair(color))
        window.refresh()
        time.sleep(0.1)
        

# Runs the model and prints the data as csv to standard output
# To write to a csv file, pipe standard output to a file like
# python3 simulate.py > file.csv
def run():

    grid = Grid()
    turtles = grid.initialize()
    w = csv.writer(sys.stdout, delimiter=',')

    w.writerow([8, cfg.TURNS])

    # Print Parameters
    w.writerow(["government-legitimacy", cfg.GOVERNMENT_LEGITIMACY])
    w.writerow(["movement?", "True" if cfg.MOVEMENT else "False"])
    w.writerow(["initial-agent-density", cfg.INITIAL_COP_DENSITY])
    w.writerow(["vision", cfg.VISION])
    w.writerow(["max-jail-turns", cfg.MAX_JAIL_TURNS])
    w.writerow(["initial-cop-density", cfg.INITIAL_AGENT_DENSITY])

    # Number of cops and agents
    agents = [turtle for turtle in turtles if turtle.getType() \
        == cfg.Type.AGENT]
    num_agents = len(agents)
    num_cops = len(turtles) - num_agents
    w.writerow(["Agents", num_agents])
    w.writerow(["Cops", num_cops])
    
    # Columns
    w.writerow(["Run", "Actives", "Jailed", "Neutral"])

    # Simulate model and print run data
    rows = []
    for i in range(0, cfg.TURNS):
        active, jailed, neutral = 0, 0, 0
        for agent in agents:
            if agent.isActive():
                active = active + 1
            elif agent.isJailed():
                jailed = jailed + 1
            else:
                neutral = neutral + 1
        rows.append([i, active, jailed, neutral])
        
        for turtle in turtles:
            turtle.update(grid)
    w.writerows(rows)

# Entry point of application
def __main__():
    cfg.initGlobals()
    if cfg.INITIAL_COP_DENSITY + cfg.INITIAL_AGENT_DENSITY > 1:
        raise Exception("sum of agent and cop densities should not be \
            greater than 1")

    curses.wrapper(simulate)
    # run()

__main__()