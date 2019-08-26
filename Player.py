class Player():
    def __init__(self, window, location = 0, size = 3, color = [255,0,0]):
        self.size = size
        self.color = color
        self.window = window
        if location == 0:
            self.location = ((self.window.size[0]) - (self.window.size[0] // 8) , self.window.size[1] // 2) #left most location
        else:
            self.location = location

        for i in range(self.location[1], self.location[1] + self.size):
            self.window.replace(self.color, (self.location[0], i))

    def contacted_ball(self, ball_location, ball_size):
        """returns a boolean value of if the ball contacted the player"""
        locations = []
        for i in range(ball_size[1]):
            locations.append((ball_location[0] + ball_size[0] - 1, ball_location[1] + i))

    def move(self, action):
        """moves the player occurding to the given action and returns if the player is out of boundary due to the taken action"""
        if action == 1:
            self.location[1] -= 1
            if self.location[1] < 0 :
                return(True)
            self.window.replace(self.color, (self.location[0], self.location[1]))
            self.window.replace([0,0,0], (self.location[0], self.location[1] + self.size + 1))
            return(False)

        elif action == 2:
            self.location[1] += 1
            if self.location >= self.window.size[1]:
                return(True)
            self.window.replace(self.color, (self.location[0], self.location[1] + self.size - 1))
            self.window.replace([0,0,0], (self.location[0], self.location[1] - 1))
            return(False)
        
        return(False)