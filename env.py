from Window import Window
from Blocks import Blocks

class Env():
    def __init__(self):
        #creating the starting enviornment
        self.window = Window((80,40))
        BLOCK_AREA = (self.window.size[0]/4, self.window.size[1])
        self.blocks = Blocks(self.window, BLOCK_AREA) 