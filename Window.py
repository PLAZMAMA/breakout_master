import numpy as np
import matplotlib.pyplot as plt

class Window():
    def __init__(self, size, background_color = 0):
        self.size = size
        self.window = np.full(self.size + (3,), background_color, dtype = np.int16)
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1,1,1)
    
    def replace(self, value, location):
        """replace an element in the window"""
        self.window[location[0], location[1]] = value
    
    def show(self):
        """displays the window in RGB"""
        window_img = np.array(self.window, dtype = np.uint8)
        self.ax1.clear()
        self.ax1.imshow(window_img)
        plt.show(block = False)