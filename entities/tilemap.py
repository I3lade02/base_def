import pygame
import random

TILE_SIZE = 32

TILE_TYPES = {
    0: (34, 177, 76),   # Grass (light green)
    1: (185, 122, 87),  # Dirt (brown)
    2: (127, 127, 127), # Stone (gray)
    3: (0, 100, 0),     # Tree (dark green)
    5: (200, 200, 0),   # House (yellow block)
    6: (150, 75, 0)     # Barracks (brownish)
}

class TileMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[0 for _ in range(width)] for _ in range(height)]  # Default all grass
        self.building_states = {}

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
    
    def start_training(self, x, y):
        self.building_states[(x, y)] = {
            'training': True,
            'progress': 0,
        }
        print(f"Started training at ({x}, {y})")

    def update_training(self):
        # ✅ Only progress here, no resetting!
        for (x, y), state in self.building_states.items():
            if state.get('training'):
                state['progress'] += 1

    def pop_finished_trainings(self):
        spawned_units = []
        finished_training = []

        for (x, y), state in self.building_states.items():
            if state.get('training') and state['progress'] >= 100:
                finished_training.append((x, y))

        for (x, y) in finished_training:
            self.building_states[(x, y)]['training'] = False
            self.building_states[(x, y)]['progress'] = 0
            spawned_units.append((x, y))
            print(f"Soldier trained at ({x}, {y})")  # ✅ Now printing here

        return spawned_units

    def draw(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                tile_type = self.tiles[y][x]
                color = TILE_TYPES.get(tile_type, (255, 0, 0))
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(surface, color, rect)

                # Draw training progress if building is training
                if (x, y) in self.building_states:
                    state = self.building_states[(x, y)]
                    if state.get('training'):
                        progress_ratio = state['progress'] / 100
                        bar_width = int(TILE_SIZE * progress_ratio)
                    
                        # Draw a thin green bar INSIDE the building
                        bar_rect = pygame.Rect(
                            rect.x, rect.y,  # starting at the top of the building
                            bar_width, 4      # 4px high
                        )
                        pygame.draw.rect(surface, (0, 255, 0), bar_rect)

    def get_tile(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        return None
    
    def set_tile(self, x, y, tile_type):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[y][x] = tile_type
