import pygame
import os

from Objects.Bullet import Bullet
from Utils.ImageLoader import ImageLoader
from Utils.Initializer import Initializer
from Utils.SoundLoader import SoundLoader
from Variable import Variable

var = Variable()
img = ImageLoader()
initer = Initializer()
sound = SoundLoader()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img.player_img, (100, 50))
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = var.WIDTH / 2
        self.rect.bottom = var.HEIGHT - 10
        self.speedx = 8
        self.speedy = 8
        self.health = 100
        self.lives = 3
        self.hidden = False
        self.hide_time = 0
        self.gun = 1
        self.gun_time = 0

    def update(self):
        now = pygame.time.get_ticks()
        if self.gun > 1 and now - self.gun_time > 5000:
            self.gun -= 1
            self.gun_time = now

        if self.hidden and now - self.hide_time > 1000:
            self.hidden = False
            self.rect.centerx = var.WIDTH / 2
            self.rect.bottom = var.HEIGHT - 10

        key_pressed = pygame.key.get_pressed()

        # Right
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx

        # Left
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx

        # Up
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speedy

        # Down
        if key_pressed[pygame.K_UP]:
            self.rect.y -= self.speedy

        # Border
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        if not (self.hidden):
            if self.gun == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                var.ALL_SPRITES.add(bullet)
                var.BULLETS.add(bullet)
                sound.shoot_sound.play()
            elif self.gun >= 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                var.ALL_SPRITES.add(bullet1)
                var.ALL_SPRITES.add(bullet2)
                var.BULLETS.add(bullet1)
                var.BULLETS.add(bullet2)
                sound.shoot_sound.play()

    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT + 500)

    def gunup(self):
        self.gun += 1
        self.gun_time = pygame.time.get_ticks()
