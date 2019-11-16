# breakout_master
trying to make the computer master the game of breakout using q-learning.

# running the program
1. clone the git repo
2. make sure you have all the packages that are in requirements.txt
3. go into your command prompt/terminal and run python in the breakout_master directory
4. paste the code below and see the network train and attempt to beat the game
from Agent import Agent
from Env import Env
agent = Agent(Env)
agent.train()
