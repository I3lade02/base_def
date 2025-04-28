import pygame
from entities.tilemap import TileMap
from entities.unit import Soldier

class GameScene:
    def __init__(self, manager):
        self.manager = manager
        self.tilemap = TileMap(40, 22)
        self.tilemap.generate()
        self.selected_building = 5  # Default --> House
        self.soldiers = []

    def update(self):
        self.tilemap.update_training()
        for (x, y) in self.tilemap.pop_finished_trainings():
            print(f"Spawning soldier at ({x}, {y})")
            self.soldiers.append(Soldier(x, y))
    
    def draw(self, surface):
        self.tilemap.draw(surface)
        for soldier in self.soldiers:
            print(f"Drawing soldier at pixel ({soldier.x * 32}, {soldier.y * 32})")
            soldier.draw(surface)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.manager.change_scene('gameover')
                elif event.key == pygame.K_1:
                    self.selected_building = 5  # House
                    print("Selected: house")
                elif event.key == pygame.K_2:
                    self.selected_building = 6  # Barracks
                    print("Selected: barracks")

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    tile_x = mouse_x // 32
                    tile_y = mouse_y // 32

                    if 0 <= tile_x < self.tilemap.width and 0 <= tile_y < self.tilemap.height:
                        clicked_tile = self.tilemap.get_tile(tile_x, tile_y)
                        print(f"Clicked tile ID: {clicked_tile}")

                        if clicked_tile == 0:
                            self.tilemap.set_tile(tile_x, tile_y, self.selected_building)

                        elif clicked_tile == 6:
                            print("barracks clicked")
                            self.tilemap.start_training(tile_x, tile_y)
