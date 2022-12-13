import pygame
import os


class Variable:
    FPS = 60
    WIDTH = 500
    HEIGHT = 600

    IDTEXT = 0
    ID = 0
    SCORE = 0

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    ALL_SPRITES = pygame.sprite.Group()
    ROCKS = pygame.sprite.Group()
    BULLETS = pygame.sprite.Group()
    POWERS = pygame.sprite.Group()

    FONT_NAME = os.path.join("../font.ttf")
