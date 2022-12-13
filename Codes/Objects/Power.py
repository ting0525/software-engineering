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


class Power(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = img.power_imgs[self.type]
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > var.HEIGHT:
            self.kill()
