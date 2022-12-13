# 太空生存戰
import pygame
import random
import os
from Variable import Variable
from ImageLoader import ImageLoader
from Initializer import Initializer
from SoundLoader import SoundLoader
from Functions import *
from Bullet import Bullet
from Explosion import Explosion
from Player import Player
from Power import Power
from Rock import Rock
import requests
# var = Variable()
img = ImageLoader()
initer = Initializer()
sound = SoundLoader()


pygame.mixer.music.play(-1)

# 遊戲迴圈
def main():
    show_init = True
    running = True
    while running:
        if show_init:
            close = frame()
            if close:
                break
            show_init = False
            player = Player()
            Variable.all_sprites.add(player)
            for i in range(8):
                new_rock()
            score = 0

        initer.clock.tick(Variable.FPS)
        # 取得輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # 更新遊戲
        Variable.all_sprites.update()
        # 判斷石頭 子彈相撞
        hits = pygame.sprite.groupcollide(Variable.rocks, Variable.bullets, True, True)
        for hit in hits:
            random.choice(sound.expl_sounds).play()
            score += hit.radius
            expl = Explosion(hit.rect.center, 'lg')
            Variable.all_sprites.add(expl)
            if random.random() > 0.9:
                pow = Power(hit.rect.center)
                Variable.all_sprites.add(pow)
                Variable.powers.add(pow)
            new_rock()

        # 判斷石頭 飛船相撞
        hits = pygame.sprite.spritecollide(player, Variable.rocks, True, pygame.sprite.collide_circle)
        for hit in hits:
            new_rock()
            player.health -= hit.radius * 2
            expl = Explosion(hit.rect.center, 'sm')
            Variable.all_sprites.add(expl)
            if player.health <= 0:
                death_expl = Explosion(player.rect.center, 'player')
                Variable.all_sprites.add(death_expl)
                sound.die_sound.play()
                player.lives -= 3
                player.health = 100
                player.hide()

        # 判斷寶物 飛船相撞
        hits = pygame.sprite.spritecollide(player, Variable.powers, True)
        for hit in hits:
            if hit.type == 'shield':
                player.health += 20
                if player.health > 100:
                    player.health = 100
                sound.shield_sound.play()
            elif hit.type == 'gun':
                player.gunup()
                sound.gun_sound.play()

        if player.lives == 0 and not (death_expl.alive()):
            show_init = True
            running = False

        # 畫面顯示
        initer.screen.fill(Variable.BLACK)
        initer.screen.blit(img.background_img, (0, 0))
        Variable.all_sprites.draw(initer.screen)
        draw_text(initer.screen, str(score), 18, Variable.WIDTH / 2, 10)
        draw_health(initer.screen, player.health, 5, 15)
        draw_lives(initer.screen, player.lives, img.player_mini_img, Variable.WIDTH - 100, 15)
        pygame.display.update()
    print(score)
    #dic = {'id' : Variable.idtext , 'score' : score}
    #print(dic)
    token = 123456
    req_get(Variable.idtext , score , token)
    