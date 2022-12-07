import pygame
from Variable import Variable
from ImageLoader import ImageLoader
from Initializer import Initializer
from SoundLoader import SoundLoader

var = Variable()
img = ImageLoader()
initer = Initializer()
sound = SoundLoader()
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img.bullet_img
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()