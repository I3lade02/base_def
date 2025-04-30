import pygame

TILE_SIZE = 32

class Soldier:
    def __init__(self, x, y, tilemap):
        self.x = x
        self.y = y
        self.color = (0, 0, 255)
        self.target_x = x 
        self.target_y = y
        self.speed = 0.1
        self.tilemap = tilemap

    def update(self):
        # Step direction first
        move_x = self.x
        move_y = self.y

        # Prioritize X movement first
        if abs(self.x - self.target_x) > 0.01:
            if self.x < self.target_x:
                move_x += self.speed
            elif self.x > self.target_x:
                move_x -= self.speed

        elif abs(self.y - self.target_y) > 0.01:
            if self.y < self.target_y:
                move_y += self.speed
            elif self.y > self.target_y:
                move_y -= self.speed

        # Check the tile we're about to move into
        next_tile_x = int(move_x)
        next_tile_y = int(move_y)
        tile_id = self.tilemap.get_tile(next_tile_x, next_tile_y)

        if tile_id == 0:  # ✅ Only walk on grass
            self.x = move_x
            self.y = move_y
        else:
            # Blocked → don't move this frame, but keep target
            pass

    def draw(self, surface):
        pixel_x = self.x * TILE_SIZE
        pixel_y = self.y * TILE_SIZE

        pygame.draw.circle(surface, self.color, (pixel_x + TILE_SIZE // 2, pixel_y + TILE_SIZE // 2), 10)
