import os

import pygame

from Class.Variable import Variable

from function import *

var = Variable()

# 遊戲初始化 and 創建視窗
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((var.WIDTH, var.HEIGHT))
pygame.display.set_caption("第一個遊戲")
clock = pygame.time.Clock()

# 載入圖片
background_img = pygame.image.load("Images/background.png").convert()
player_img = pygame.image.load("Images/player.png").convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(var.BLACK)
pygame.display.set_icon(player_mini_img)
bullet_img = pygame.image.load("Images/bullet.png").convert()
rock_imgs = []
for i in range(7):
    rock_imgs.append(pygame.image.load(os.path.join("Images", f"rock{i}.png")).convert())
expl_anim = {'lg': [], 'sm': [], 'player': []}
for i in range(9):
    expl_img = pygame.image.load(os.path.join("Images", f"expl{i}.png")).convert()
    expl_img.set_colorkey(var.BLACK)
    expl_anim['lg'].append(pygame.transform.scale(expl_img, (75, 75)))
    expl_anim['sm'].append(pygame.transform.scale(expl_img, (30, 30)))
    player_expl_img = pygame.image.load(os.path.join("Images", f"player_expl{i}.png")).convert()
    player_expl_img.set_colorkey(var.BLACK)
    expl_anim['player'].append(player_expl_img)
power_imgs = {'shield': pygame.image.load("Images/shield.png").convert(),
              'gun': pygame.image.load("Images/gun.png").convert()}

# 載入音樂、音效
shoot_sound = pygame.mixer.Sound("Sound/shoot.wav")
gun_sound = pygame.mixer.Sound("Sound/pow1.wav")
shield_sound = pygame.mixer.Sound("Sound/pow0.wav")
die_sound = pygame.mixer.Sound("Sound/rumble.ogg")
expl_sounds = [
    pygame.mixer.Sound("Sound/expl0.wav"),
    pygame.mixer.Sound("Sound/expl1.wav")
]
pygame.mixer.music.load("Sound/background.ogg")
pygame.mixer.music.set_volume(0.4)


font_name = os.path.join("font.ttf")

