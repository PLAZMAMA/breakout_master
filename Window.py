import numpy as np
import cv2

class Window():
    def __init__(self, shape, background_color = 0):
        self.shape = shape
        self.window = np.full(self.shape + (3,), background_color, dtype = np.int16)
    
    def replace(self, value, location):
        """replace an element in the window"""
        self.window[location[0], location[1]] = value
    
    def show(self):
        """displays the window in RGB"""
        cv2.imshow(self.window)