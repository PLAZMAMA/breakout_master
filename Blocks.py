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
    
    def destroy_contacting_blocks(self, ball_location):
        """checks if a block is contacting the ball and destroys it"""
        for block in self.blocks:
            if block.hit():
                block.delete()