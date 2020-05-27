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
  p = sh.run(command, stdout=sh.PIPE)
  lines = p.stdout.decode("utf-8")
  
  # Get data
  skip = int(lines.split('\n')[0].split(',')[0])
  file = io.StringIO(lines)
  df = pandas.read_csv(file, delimiter=',', skiprows=skip+1)

  # Plot time vs actives, jailed, neutral
  fig = df.plot.line(x='Run')
  fig.set_xlabel('Run')
  fig.get_figure().savefig(name + '_actives-vs-time.png')
  
  # waiting times distribution
  threshold = 50
  df1 = df[df['Actives'] > threshold] # runs where there is a riot
  df2 = df1[df1.shift(1)['Run'] != df1['Run']-1]  # runs where a riot starts
  df3 = df2['Run'][1:].reset_index(drop=True) - \
      df2['Run'][:-1].reset_index(drop=True)      # waiting times
  fig = df3.plot.hist(bins=range(1,100))
  fig.get_figure().savefig(name + '_waiting_times_hist.png')


def __main__():

  # experiments = [("one","tw")]
  experiments = [
    ("exp1", {
      "government_legitimacy": 0.82,
      "turns": 10,
    }), 
    # ("exp2", {
    #   "government_legitimacy": 0.9
    # })
  ]

  for name, params in experiments:
    runExperiment(name, params)




__main__()
