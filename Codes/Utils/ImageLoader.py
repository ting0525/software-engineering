import pygame
import os

from Utils.Initializer import Initializer
from Variable import Variable

var = Variable()
initer = Initializer()


class ImageLoader:
    # 載入圖片
    Image_folder = "../Images"
    Button = "../Images/Button"
    Expl = "../Images/Expl"
    Player_expl = "../Images/Player_expl"
    Rock = "../Images/Rock"
    Background = "../Images/Background"

    # Background images
    background_img = pygame.image.load(os.path.join(Background, "background.png")).convert()
    background_img2 = pygame.image.load(os.path.join(Background, "background2.jpg")).convert()
    game_background = pygame.image.load(os.path.join(Background, "game_background.jpg")).convert()


    # Player images
    player_img = pygame.image.load(os.path.join(Image_folder, "player.png")).convert()
    player_mini_img = pygame.transform.scale(player_img, (25, 19))
    player_mini_img.set_colorkey(var.BLACK)
    pygame.display.set_icon(player_mini_img)

    # Bullet images
    bullet_img = pygame.image.load(os.path.join(Image_folder, "bullet.png")).convert()

    # Rock images
    rock_imgs = []
    for i in range(7):
        rock_imgs.append(pygame.image.load(os.path.join(Rock, f"rock{i}.png")).convert())

    # Expl images
    expl_anim = {'lg': [], 'sm': [], 'player': []}
    for i in range(9):
        expl_img = pygame.image.load(os.path.join(Expl, f"expl{i}.png")).convert()
        expl_img.set_colorkey(var.BLACK)
        expl_anim['lg'].append(pygame.transform.scale(expl_img, (75, 75)))
        expl_anim['sm'].append(pygame.transform.scale(expl_img, (30, 30)))
        player_expl_img = pygame.image.load(os.path.join(Player_expl, f"player_expl{i}.png")).convert()
        player_expl_img.set_colorkey(var.BLACK)
        expl_anim['player'].append(player_expl_img)

    # Power images
    power_imgs = {'shield': pygame.image.load(os.path.join(Image_folder, "shield.png")).convert(),
                  'gun': pygame.image.load(os.path.join(Image_folder, "gun.png")).convert()}
