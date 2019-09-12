class Block():
    def __init__(self, window, location, size = (1,4), color = [255,255,0]):
        self.size = size
        self.window = window
        self.location = location #the left most location of the block
        self.upper_neighboring_locations = [[self.location[0] - 1, i] for i in range(self.location[1] - 1, self.location[1] + self.size[1] + 1)]
        self.lower_neighboring_locations =  [[self.location[0] + self.size[0], i] for i in range(self.location[1] + self.size[0], self.location[1] + self.size[1] + 1)]
        self.side_neighboring_locations = []
        for i in range(self.size[0]):
            self.side_neighboring_locations += [self.location[0] + i, self.location[1] - 1] + [self.location[0] + i, self.location[1] + self.size[1]]

        for i in range(self.location[0], self.location[0] + self.size[0]):
            for ii in range(self.location[1], self.location[1] + self.size[1]):
                self.window.replace(color, (self.location[0], i))



    def hit_ball_on_top(self, ball_locations):
        """returns a boolean value of if the ball hit the block on the top"""
        if ball_locations in self.upper_neighboring_locations:
            return(True)

        return(False)
    
    def hit_ball_on_buttom(self, ball_locations):
        """returns a boolean value of if the ball hit the block on the buttom"""
        if ball_locations in self.lower_neighboring_locations:
            return(True)
        
        return(False)

    def hit_ball_on_side(self, ball_locations):
        """returns a boolean value of if the ball hit the block on the size"""
        if ball_locations in self.side_neighboring_locations:
            return(True)
        
        return(False)
    
    def hit(self, ball_locations):
        """returns a boolean value of if the ball hit the block in any place"""
        if self.hit_ball_on_buttom(ball_locations) or self.hit_ball_on_side(ball_locations) or self.hit_ball_on_top(ball_locations):
            return(True)

        return(False)
        
    def delete(self):
        """deletes the displayed image of the block"""
        for i in range(self.location[1], self.location[1] + self.size):
            self.window.replace([0,0,0], (self.location[0], i)) 