import random

class Ball():
    def __init__(self, window, size = (2,2), color = [0,0,255], location = 0, starting_direction = (random.randint(-2, -1), random.choice([-1, 1]))): 
        self.direction = starting_direction
        self.color = color
        self.size = size
        self.window = window
        if location == 0:
            self.location = (self.window.size[0] // 2, self.window.size[1] // 2)
        else:
            self.location = location

        for i in range(self.size[0]):
            for ii in range(self.size[1]):
                self.window.replace(self.color, (self.location[0] + i, self.location[1] + ii))
        
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

    def move_slope(self, slope):
        """moves the ball given a slope (rise/y,run/x)"""
        if abs(slope[0]) == slope[0]:
            for _ in range(slope[0]):
                self.move(0)
        else:
            for _ in range(abs(slope[0])):
                self.move(1)

        if abs(slope[1]) == slope[1]:
            for _ in range(slope[1]):
                self.move(3)
        else:
            for _ in range(abs(slope[1])):
                self.move(2)

    def get_surrounding_locations(self):
        """return the balls surrounding locations"""
        ball_locations = []
        for i in range(self.size[0]):
            for ii in range(self.size[1]):
                ball_locations.append((self.location[0] + i, self.location[1] + ii))
        
        return(ball_locations)

    def flip_number(self, number):
        """flips the sign of the given number"""
        if number < 0:
            return(abs(number))
        return(-number)
    
    def change_direction(self, hit_player, hit_block_on_side, hit_block_on_buttom, hit_block_on_top):
        """changes the balls direction by looking if it hit any objects or the bounderys of the window"""
        if self.location[0] >= 0 or self.location[1] >= 0 or self.location[0] <= self.window.size[0] or self.location <= self.window.size[1]:
            self.direction[1] = self.flip_number(self.direction[1])
        elif hit_player:
            self.direction[0] = self.flip_number(self.direction[0])
            self.direction[1] = self.flip_number(self.direction[1])
        elif hit_block_on_side:
            self.direction[1] = self.flip_number(self.direction[1])
        elif hit_block_on_buttom:
            self.direction[0] = self.flip_number(self.direction[0])
            self.direction[1] = self.flip_number(self.direction[1])
        elif hit_block_on_top:
            self.direction[0] = self.flip_number(self.direction[0])
            self.direction[1] = self.flip_number(self.direction[1])
    
    def movement(self, hit_player, blocks):
        """moves and bounces the ball around the window """
        locations = self.get_surrounding_locations()
        for block in blocks.blocks:
            self.change_direction(hit_player, block.hit_block_on_side(locations), block.hit_block_on_buttom(locations), block.hit_block_on_top(locations))
        self.move_slope(self.direction)