import pygame

TILE_SIZE = 32

class Soldier:
    def __init__(self, x, y):
        self.x = x  # grid coordinate (tile-based)
        self.y = y
        self.color = (0, 0, 255)  # Blue color

    def draw(self, surface):
        # Convert grid position to pixel position
        pixel_x = self.x * TILE_SIZE
        pixel_y = self.y * TILE_SIZE

        # Draw small blue circle in the center of the tile
        print(f"Drawing soldier at pixel ({self.x * TILE_SIZE}, {self.y * TILE_SIZE})")
        pygame.draw.circle(surface, self.color, (pixel_x + TILE_SIZE // 2, pixel_y + TILE_SIZE // 2), 10)
