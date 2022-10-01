import pygame
import os
from Variable import Variable
from Initializer import Initializer
var = Variable()
initer = Initializer()
class ImageLoader:


    # 載入圖片
    img = "../Images"
    background_img = pygame.image.load(os.path.join("%s" % img, "background.png")).convert()
    player_img = pygame.image.load(os.path.join(img, "player.png")).convert()
    player_mini_img = pygame.transform.scale(player_img, (25, 19))
    player_mini_img.set_colorkey(var.BLACK)
    pygame.display.set_icon(player_mini_img)
    bullet_img = pygame.image.load(os.path.join(img, "bullet.png")).convert()
    rock_imgs = []
    for i in range(7):
        rock_imgs.append(pygame.image.load(os.path.join(img, f"rock{i}.png")).convert())
    expl_anim = {'lg': [], 'sm': [], 'player': []}
    for i in range(9):
        expl_img = pygame.image.load(os.path.join(img, f"expl{i}.png")).convert()
        expl_img.set_colorkey(var.BLACK)
        expl_anim['lg'].append(pygame.transform.scale(expl_img, (75, 75)))
        expl_anim['sm'].append(pygame.transform.scale(expl_img, (30, 30)))
        player_expl_img = pygame.image.load(os.path.join(img, f"player_expl{i}.png")).convert()
        player_expl_img.set_colorkey(var.BLACK)
        expl_anim['player'].append(player_expl_img)
    power_imgs = {'shield': pygame.image.load(os.path.join(img, "shield.png")).convert(),
                  'gun': pygame.image.load(os.path.join(img, "gun.png")).convert()}
