import numpy as np
from cv2 import imshow

class Window():
    def __init__(self, size, background_color = 0):
        self.size = size
        self.window = np.full(self.size + (3,), background_color, dtype = np.int16)
    
    def replace(self, value, location):
        """replace an element in the window"""
        self.window[location[0], location[1]] = value
    
    def show(self):
        """displays the window in RGB"""
        imshow("env", self.window)