class Player():
    def __init__(self, window, location = 0, size = (1,5), color = [255,0,0]):
        self.size = size
        self.color = color
        self.window = window
        if location == 0:
            self.location = [(self.window.size[0]) - (self.window.size[0] // 8) , (self.window.size[1] // 2) - self.size[1] // 2]
        else:
            self.location = location

        for i in range(self.location[0], self.location[0] + self.size[0]):
            for ii in range(self.location[1], self.location[1] + self.size[1]):
                self.window.replace(self.color, (i, ii))

    def contacted_ball(self, ball_location, ball_size):
        """returns a boolean value of if the ball contacted the player"""
        if (ball_location[0] + ball_size[0] - 1 == self.location[0] - 1) and ((ball_location[1] + ball_size[1] - 1 >= self.location[1] and ball_location[1] + ball_size[1] - 1 <= self.location[1] + self.size[1] - 1) or (ball_location[1] <= self.location[1] + self.size[1] - 1 and ball_location[1] >= self.location[1])):
            return(True)
        return(False)

    def move(self, action):
        """moves the player occurding to the given action unless the player hit the boundary
        0 : no movement
        1 : left movement
        2 : right movement
        """
        if action == 1:
            if self.location[1] > 0: 
                self.location[1] -= 1
                for i in range(self.location[0], self.location[0] + self.size[0]):
                    self.window.replace(self.color, (i, self.location[1]))
                    self.window.replace([0,0,0], (i, self.location[1] + self.size[1]))

        elif action == 2:
            if self.location[1] + self.size[1] - 1 < self.window.size[1] - 1:
                self.location[1] += 1
                for i in range(self.location[0], self.location[0] + self.size[0]):
                    self.window.replace(self.color, (i, self.location[1] + self.size[1] - 1))
                    self.window.replace([0,0,0], (i, self.location[1] - 1))
                