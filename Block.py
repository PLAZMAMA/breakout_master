class Block():
    def __init__(self, window, location, size = 4, color = [255,255,0]):
        self.size = size
        self.window = window
        self.location = location #the left most location of the block
        self.neighboring_locations = [[self.location[0] + 1, i] for i in range(self.location[1] - 1, self.location[1] + size + 1)] + [[self.location[0] - 1, i] for i in range(self.location[1] - 1, self.location[1] + size + 1)]
        self.neighboring_locations.append([self.location[0], self.location[1] - 1])
        self.neighboring_locations.append([self.location[0], self.location[1] + size])
        for i in range(self.location[1], self.location[1] + self.size):
            self.window.replace(color, (self.location[0], i))



    def hit(self, ball_location):
        """returns a boolean value of it the ball hit it"""
        if ball_location in self.neighboring_locations:
            return(True)
        return(False)
    
    def delete(self):
        """deletes the displayed image of the block"""
        for i in range(self.location[1], self.location[1] + self.size):
            self.window.replace([0,0,0], (self.location[0], i))