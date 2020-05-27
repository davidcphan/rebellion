import subprocess as sh
import io
import pandas
import matplotlib.pyplot as plt

defaults = {
  "initial_cop_density": 0.04,
  "initial_agent_density": 0.7,
  "vision": 7,
  "government_legitimacy": 0.82,
  "max_jail_turns": 30,
  'turns': 10,
}

def makeRunCommand(params):
  default_params = defaults.copy()
  for param, value in params.items():
    default_params[param] = value
  command = ["python3", "simulate.py"]
  for param, value in default_params.items():
    param = param.replace('_', '-')
    param = "--" + param
    command.extend([param, str(value)])
  return command

def runExperiment(name, params):
  # Run command
  command = makeRunCommand(params)
  print(command)
  p = sh.run(command, stdout=sh.PIPE)
  lines = p.stdout.decode("utf-8")
  print(lines)
  # Get data
  skip = int(lines.split('\n')[0].split(',')[0])
  file = io.StringIO(lines)
  data = pandas.read_csv(file, delimiter=',', skiprows=skip+1)

  # Plot time vs actives, jailed, neutral
  fig = data.plot.line(x='Run')
  fig.set_xlabel('Run')
  fig.get_figure().savefig(name + '_actives-vs-time.png')
  
  # waiting times distribution
  # riot size distribution 


def __main__():

  # experiments = [("one","tw")]
  experiments = [
    ("default", {
    "initial_cop_density": 0.04,
    "initial_agent_density": 0.7,
    "vision": 7,
    "government_legitimacy": 0.80,
    "max_jail_turns": 30,
    'turns': 100,
    }),
     ("gov_high", {
    "initial_cop_density": 0.04,
    "initial_agent_density": 0.7,
    "vision": 7,
    "government_legitimacy": 0.90,
    "max_jail_turns": 30,
    'turns': 100,
    }),
    ("gov_low", {
    "initial_cop_density": 0.04,
    "initial_agent_density": 0.7,
    "vision": 7,
    "government_legitimacy": 0.20,
    "max_jail_turns": 30,
    'turns': 100,
    }),
    ("cop_high", {
    "initial_cop_density": 0.15,
    "initial_agent_density": 0.7,
    "vision": 7,
    "government_legitimacy": 0.80,
    "max_jail_turns": 30,
    'turns': 100,
    }),
    ("cop_low", {
    "initial_cop_density": 0.02,
    "initial_agent_density": 0.7,
    "vision": 7,
    "government_legitimacy": 0.80,
    "max_jail_turns": 30,
    'turns': 100,
    }),
    ("agent_high", {
    "initial_cop_density": 0.04,
    "initial_agent_density": 0.9,
    "vision": 7,
    "government_legitimacy": 0.80,
    "max_jail_turns": 30,
    'turns': 100,
    }),
    ("agent_low", {
    "initial_cop_density": 0.04,
    "initial_agent_density": 0.3,
    "vision": 7,
    "government_legitimacy": 0.80,
    "max_jail_turns": 30,
    'turns': 100,
    }),
    ("vision_high", {
    "initial_cop_density": 0.04,
    "initial_agent_density": 0.7,
    "vision": 15,
    "government_legitimacy": 0.80,
    "max_jail_turns": 30,
    'turns': 100,
    }),
    ("vision_low", {
    "initial_cop_density": 0.04,
    "initial_agent_density": 0.7,
    "vision": 2,
    "government_legitimacy": 0.80,
    "max_jail_turns": 30,
    'turns': 100,
    }),
    ("jail_high", {
    "initial_cop_density": 0.04,
    "initial_agent_density": 0.7,
    "vision": 7,
    "government_legitimacy": 0.80,
    "max_jail_turns": 50,
    'turns': 100,
    }),
    ("jail_low", {
    "initial_cop_density": 0.04,
    "initial_agent_density": 0.7,
    "vision": 7,
    "government_legitimacy": 0.80,
    "max_jail_turns": 5,
    'turns': 100,
    }),

  ]

  for name, params in experiments:
    runExperiment(name, params)




__main__()
