import pygame
from entities.tilemap import TileMap

class GameScene:
    def __init__(self, manager):
        self.manager = manager
        self.tilemap = TileMap(40, 22)
        self.tilemap.generate()

    def update(self):
        pass
    
    def draw(self, surface):
        self.tilemap.draw(surface)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.manager.change_scene('gameover')