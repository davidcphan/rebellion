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
    ("exp1", {
      "government_legitimacy": 0.82
    }), 
    # ("exp2", {
    #   "government_legitimacy": 0.9
    # })
  ]

  for name, params in experiments:
    runExperiment(name, params)




__main__()
