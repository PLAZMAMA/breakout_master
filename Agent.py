import numpy as np

class Agent():
    def __init__(self, Env):
        self.env = Env()
        self.env.reset()
        self.q_table = np.random.uniform(size =  ([self.env.observation_space, self.env.action_space.n]))

    def train(self, show_every = 500, starting_epsilon = 0, learning_rate = 0.7, discount_factor = 0.1, episoides = 20000):
        """trains the agent"""
        observation = self.env.reset()
        done = False
        for episode in episoides:
            #increasing the discount factor as the learning goes
            if (discount_factor < 0.9) and (episode % (episoides // 8) == 0):
                discount_factor += 0.1
            while not(done):
                action = np.argmax(self.q_table[observation])
                new_observation, reward, done = self.env.step(action)
                current_q = np.max(self.q_table[observation])
                if done:
                    new_q = (1 - learning_rate) * current_q + learning_rate * (reward + discount_factor)
                elif len(self.env.blocks.blocks) == 0:
                    done = True
                    new_q = reward
                    print("success!!")
                    
                else:
                    max_future_q = np.max(self.q_table[new_observation])
                    new_q = (1 - learning_rate) * current_q + learning_rate * (reward + discount_factor * max_future_q)

                self.q_table[observation + [action]] = new_q
                observation = new_observation
