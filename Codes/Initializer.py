import pygame
from Variable import Variable
var = Variable()
class Initializer:
    # 遊戲初始化 and 創建視窗
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((var.WIDTH, var.HEIGHT))
    pygame.display.set_caption("第一個遊戲")
    clock = pygame.time.Clock()