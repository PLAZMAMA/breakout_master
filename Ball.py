class Ball():
    def __init__(self, window, size = (2,2), color = [0,0,255], location = 0):
        self.color = color
        self.size = size
        self.window = window
        if location == 0:
            self.location = (self.window.size[0] // 2, self.window.size[1] // 2)
        else:
            self.location = location

        for i in range(self.size[0]):
            for ii in range(self.size[1]):
                self.window.replace(self.color, (self.location + i, self.location + ii))
        
    def move(self, direction):
        """
        moves the ball given the direction
        up: 0
        down: 1
        left: 2
        right: 3
        """
        if direction == 0:
            for i in range(self.location[1], self.size[1]):
                self.window.replace([0,0,0], (self.location[0] + self.size[0] - 1, i))
                self.window.replace(self.color, (self.location[0] - 1, i))

            self.location[0] -= 1

        elif direction == 1:
            for i in range(self.location[1], self.size[1]):
                self.window.replace([0,0,0], (self.location[0], i))
                self.window.replace(self.color, (self.location[0] + self.size[0], i))
            
            self.location[0] += 1
        
        elif direction == 2:
            for i in range(self.location[0], self.size[0]):
                self.window.replace([0,0,0], (i, self.location[1] + self.size[1] - 1))
                self.window.replace(self.color, (i, self.location[1] - 1))
            
            self.location[1] -= 1
        
        elif direction == 3:
            for i in range(self.location[0], self.size[0]):
                self.window.replace([0,0,0], (i, self.location[1]))
                self.window.replace(self.color, (i, self.location[1] + self.size))
            
            self.location[1] += 1

    def movement(self, slope, contacted_player, contacted_block):
        """moves and bounces the ball given a slope"""