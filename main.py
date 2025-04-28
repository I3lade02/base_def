import pygame
import sys
from scenes.menu import MenuScene
from scenes.game import GameScene
from scenes.gameover import GameOverScene

#python initialize
pygame.init()

#settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

#window setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Base defense")
clock = pygame.time.Clock()

#scene manager
class SceneManager:
    def __init__(self):
        self.scenes = {
            'menu':MenuScene(self),
            'game':GameScene(self),
            'gameover':GameOverScene(self)
        }
        self.current_scene = self.scenes['menu']
    
    def change_scene(self, scene_name):
        if scene_name in self.scenes:
            self.current_scene = self.scenes[scene_name]

    def update(self):
        self.current_scene.update()

    def draw(self, surface):
        self.current_scene.draw(surface)

    def handle_events(self, events):
        self.current_scene.handle_events(events)

def main():
    manager = SceneManager()

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        manager.handle_events(events)
        manager.update()

        screen.fill((30, 30, 30))
        manager.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()