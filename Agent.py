import numpy as np
import time

class Agent():
    def __init__(self, Env, q_table_name = ""):
        self.env = Env()
        self.env.reset() #reseting to get the action and observation spaces
        self.q_table = np.random.uniform(low = -1.0, high = 0.0,size = (self.env.observation_space + [self.env.action_space.n]))

    def train(self, episodes = 20000, show_every = 500, show_stats_every = 1000, learning_rate = 0.7, discount_factor = 0.1):
        """trains the agent"""
        if show_every == -1:
            show_every = episodes + 1
        observation = self.env.reset()
        avrage = 0
        for episode in range(episodes):
            #increasing the discount factor as the learning goes
            if (discount_factor < 0.8) and (episode % (episodes // 8) == 0):
                discount_factor += 0.1
            time_played = 0
            done = False
            while not(done):
                action = np.argmax(self.q_table[observation])
                new_observation, reward, done = self.env.step(action)
                current_q = np.max(self.q_table[observation])
                if done:
                    new_q = (1 - learning_rate) * current_q + learning_rate * (reward + discount_factor)

                elif len(self.env.blocks.blocks) == 0:
                    done = True
                    new_q = reward
                    
                else:
                    max_future_q = np.max(self.q_table[new_observation])
                    new_q = (1 - learning_rate) * current_q + learning_rate * (reward + discount_factor * max_future_q)
                    time_played += 1

                self.q_table[observation + (action, )] = new_q
                observation = new_observation

                if episode % show_every == 0:
                    self.env.render()
            
            observation = self.env.reset()
            avrage += time_played
            if episode % show_stats_every == 0:
                print(f"on episode: {episode}, avrage: {avrage // show_stats_every}")
                avrage = 0