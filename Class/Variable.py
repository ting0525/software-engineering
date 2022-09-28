import os.path

import pygame.sprite

class Variable:

    def __init__(self) -> None:
        self.FPS = 60
        self.WIDTH = 500
        self.HEIGHT = 600

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.font_name = os.path.join("../font.ttf")
        self.all_sprites = pygame.sprite.Group()
        self.rocks = pygame.sprite.Group()

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)

