from Block import Block
import random

class Blocks():
    def __init__(self, window, block_area, block_size = 4, block_limit = 0):
        if block_limit == 0:
            BLOCK_LIMIT = (block_area[0] * block_area[1] / block_size) // 2
        else:
            BLOCK_LIMIT = block_limit 

        row = 0
        self.blocks = []
        blocks_placed = 0
        while row <= block_area[0] and blocks_placed <= BLOCK_LIMIT:
            column = random.randint(0, block_area[1] // 10)
            while True:
                self.blocks.append(Block(window, (row, column), block_size))
                column += block_size + random.randint(0, block_area[1] // 10)
                blocks_placed += 1
                if column + block_size > block_area[1]:
                    break
    
    def destroy_contacting_blocks(self, ball_location, ball_size):
        """checks if a block is contacting the ball and destroys it. returns if the ball contancted one of the balls"""
        ball_locations = []
        for i in range(ball_size[0]):
            for ii in range(ball_size[1]):
                ball_locations.append((ball_location[0] + i, ball_location[1] + ii))
        c = 0
        for block in self.blocks:
            if block.hit(ball_locations):
                block.delete()
                c += 1
        if c > 0:
            return(True)
        return(False)
