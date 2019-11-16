from Window import Window
from Blocks import Blocks
from Player import Player
from Ball import Ball
from gym import spaces
from matplotlib import animation
import matplotlib.pyplot as plt

class Env():
    def __init__(self):
        self.action_space = spaces.Discrete(3)

    def observation(self):
        """returns the current observations"""
        player_observation = self.player.location[1]
        ball_observation = self.window.size[1] * self.ball.location[0] + self.ball.location[1]
        return((player_observation, ball_observation))
    
    def done(self):
        """returns if the enviornment is done(if the ball is below the player)"""
        if self.ball.location[0] >= self.player.location[0]:
            return(True)
        return(False)  

    def render(self):
        """displays the enviornment"""
        self.window.show()
    
    def reset(self):
        """resets the enviornment and returns the begining observation"""
        try:
            plt.close(self.window.fig)
        except:
            print("couldn't close the windows image/figure")
        self.window = Window((80,40))
        BLOCK_AREA = (self.window.size[0]/4, self.window.size[1])
        self.blocks = Blocks(self.window, BLOCK_AREA)
        self.player = Player(self.window)
        self.ball = Ball(self.window)
        self.observation_space = [self.window.size[1], (self.window.size[0] * self.window.size[1])]
        return(self.observation())
    
    def step(self, action):
        """takes an action, preforms it in the enviornment and returns the new observation, reward and if the env is done(weather its time to reset the env)"""
        self.player.move(action)
        ball_hit_player = self.player.contacted_ball(self.ball.location, self.ball.size)
        self.ball.movement(ball_hit_player, self.blocks)
        if ball_hit_player:
            reward = 1
        else:
            reward = -1
        return(self.observation(), reward, self.done())