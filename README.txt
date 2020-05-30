This info was extracted from the README.md from git so formatting may not be too clear.  If it is hard to read simply load the README.md file

Assignment 2 - Modelling Complex Software Systems

To modify the parameters of the simulation, the config file can be used. Setting the --average-hardship flag will cause our extension, which causes the grievance of neighbours to affect an individuals grievance, to be active.

## Build and running the model
The model can be run for 20 iterations with
```
python3 simulate.py --turns 20

```
The CSV data is written directly to standard output.
To write to a file use the bash pipe operator.
```
python3 simulate.py > data.csv
```
Use the `--simulate` flag to run a graphical simulation.
Make sure your terminal is resized large enough otherwise the application
will crash.


Use the `--average-hardship` and `--active-cops` to run extension 1
and 2 as defined in our report.

Use the `--help` flag for more information.
```
$ python3 simulate.py --help
usage: simulate.py [-h] [--turns TURNS] [--initial-cop-density COP_DENSITY]
                   [--initial-agent-density AGENT_DENSITY] [--vision VISION]
                   [--government-legitimacy GOVERNMENT_LEGITIMACY]
                   [--max-jail-turns MAX_JAIL_TURNS] [--no-movement]
                   [--active-cops] [--average-hardship] [--simulate]
                   [--width WIDTH] [--height HEIGHT]

Rebellion model parameters

optional arguments:
  -h, --help            show this help message and exit
  --turns TURNS         Number of iterations for which the model runs
                        (default: 10)
  --initial-cop-density COP_DENSITY
                        Percentage of board that is cops (default: 0.04)
  --initial-agent-density AGENT_DENSITY
                        Percentage of board that is agents (default: 0.7)
  --vision VISION       Number of grid positions in north/south/east/west
                        directions that a agent/cop can see (default: 7)
  --government-legitimacy GOVERNMENT_LEGITIMACY
  --max-jail-turns MAX_JAIL_TURNS
  --no-movement         Stops agents and cops from moving (default: True)
  --active-cops         Enable extension 2 - whether cops can also behave like
                        agents (default: False)
  --average-hardship    Enable extension 1 - whether an agent's hardship is
                        affected by the average hardship of agents in their
                        vision (default: False)
  --simulate            Turns on graphical simulation (default: False)
  --width WIDTH         Width of the grid (default: 40)
  --height HEIGHT       Height of the grid (default: 20)
```

The data for our experiments was generated, collected and visualised with the `experiments.py` script.
Since there are no graphing libraries in the python standard library and this file
isn't required to run the model, we chose to use external dependencies.
This script requires `matplotlib` and `pandas` to be pip installed.
```
pip3 install matplotlib pandas
```
