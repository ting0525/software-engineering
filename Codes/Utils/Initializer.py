import pygame
from Variable import Variable
var = Variable()
class Initializer:
    # 遊戲初始化 and 創建視窗
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("太空生存戰")
    clock = pygame.time.Clock()