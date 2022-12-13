import pygame
import random

from Utils.ImageLoader import ImageLoader
from Utils.Initializer import Initializer
from Utils.SoundLoader import SoundLoader
from Variable import Variable

var = Variable()
img = ImageLoader()
initer = Initializer()
sound = SoundLoader()


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = random.choice(img.rock_imgs)
        self.image_ori.set_colorkey(var.BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(0, var.WIDTH - self.rect.width)
        self.rect.y = random.randrange(-180, -100)
        self.speedy = random.randrange(2, 5)
        self.speedx = random.randrange(-3, 3)
        self.total_degree = 0
        self.rot_degree = random.randrange(-3, 3)

    def rotate(self):
        self.total_degree += self.rot_degree
        self.total_degree = self.total_degree % 360
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > var.HEIGHT or self.rect.left > var.WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, var.WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)
