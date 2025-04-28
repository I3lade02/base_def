import pygame

class MenuScene:
    def __init__(self, manager):
        self.manager = manager

    def update(self):
        pass

    def draw(self, surface):
        surface.fill((50, 50, 100))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.manager.change_scene('game')