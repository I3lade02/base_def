import pygame
import random

TILE_SIZE = 32

TILE_TYPES = {
    0: (34, 177, 76),   # Grass
    1: (185, 122, 87),  # Dirt
    2: (127, 127, 127), # Stone
    3: (0, 100, 0)      # Tree
}

class TileMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[0 for _ in range(width)] for _ in range(height)]  # Default all grass

    def generate(self):
        for y in range(self.height):
            for x in range(self.width):
                r = random.random()
                if r < 0.05:
                    self.tiles[y][x] = 3  # Tree
                elif r < 0.1:
                    self.tiles[y][x] = 2  # Stone
                elif r < 0.2:
                    self.tiles[y][x] = 1  # Dirt
                else:
                    self.tiles[y][x] = 0  # Grass

    def draw(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                tile_type = self.tiles[y][x]
                color = TILE_TYPES[tile_type]
                pygame.draw.rect(
                    surface,
                    color,
                    (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                )

    def get_tile(self, x, y):
        #returns tile type at a given position
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        return None
    
    def set_tile(self, x, y, tile_type):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[y][x] = tile_type