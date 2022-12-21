import random
import urllib.request

import pygame
import os
import sys

from Button import Button
from Objects.Explosion import Explosion
from Objects.Player import Player
from Objects.Power import Power
from Utils.Functions import frame, new_rock, draw_text, draw_health, draw_lives, req_get
from Utils.ImageLoader import ImageLoader
from Utils.Initializer import Initializer
from Utils.SoundLoader import SoundLoader
from Variable import Variable

pygame.init()
initer = Initializer()
sound = SoundLoader()
img = ImageLoader()

SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("太空生存戰")

# Background image
BG = pygame.image.load("../Images/Background/background2.jpg")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("../font.ttf", size)


def play():
    pygame.mixer.music.play(-1)

    show_init = True
    running = True
    while running:
        if show_init:
            close = frame()
            if close:
                break
            show_init = False
            player = Player()
            Variable.ALL_SPRITES.add(player)

            for i in range(16):
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
        Variable.ALL_SPRITES.update()

        # 判斷石頭 子彈相撞
        hits = pygame.sprite.groupcollide(Variable.ROCKS, Variable.BULLETS, True, True)
        for hit in hits:
            random.choice(sound.expl_sounds).play()
            score += hit.radius
            expl = Explosion(hit.rect.center, 'lg')
            Variable.ALL_SPRITES.add(expl)
            if random.random() > 0.9:
                pow = Power(hit.rect.center)
                Variable.ALL_SPRITES.add(pow)
                Variable.POWERS.add(pow)
            new_rock()

        # 判斷石頭 飛船相撞
        hits = pygame.sprite.spritecollide(player, Variable.ROCKS, True, pygame.sprite.collide_circle)
        for hit in hits:
            new_rock()
            player.health -= hit.radius * 2
            expl = Explosion(hit.rect.center, 'sm')
            Variable.ALL_SPRITES.add(expl)
            if player.health <= 0:
                death_expl = Explosion(player.rect.center, 'player')
                Variable.ALL_SPRITES.add(death_expl)
                sound.die_sound.play()
                player.lives -= 3
                player.health = 100
                player.hide()

        # 判斷寶物 飛船相撞
        hits = pygame.sprite.spritecollide(player, Variable.POWERS, True)
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
        initer.screen.blit(img.game_background, (0, 0))
        Variable.ALL_SPRITES.draw(initer.screen)
        draw_text(initer.screen, str(score), 18, Variable.WIDTH / 2, 10)
        draw_health(initer.screen, player.health, 5, 15)
        draw_lives(initer.screen, player.lives, img.player_mini_img, Variable.WIDTH - 100, 15)
        pygame.display.update()
    print(score)
    # dic = {'id' : Variable.idtext , 'score' : score}
    # print(dic)
    token = 123456
    req_get(Variable.IDTEXT, score, token)


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect()
        SCREEN.blit(img.background_img2, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(300, 400),
                              text_input="Back", font=get_font(50), base_color="Black", hovering_color="White")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def url():
    while True:
        urllib.request.urlopen('http://127.0.0.1:80/')


def main_menu():
    pygame.mixer.music.play(-1)

    while True:

        SCREEN.blit(BG, (0, 0))

        # Getting Mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Main Menu
        MENU_TEXT = get_font(100).render("太空生存戰", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(300, 100))

        # Play button setup
        PLAY_BUTTON = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(300, 250),
                             text_input="開始", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        # Option button setup
        OPTIONS_BUTTON = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(300, 400),
                                text_input="選項", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        # Url button setup
        URL_BUTTON = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(300, 550),
                            text_input="URL", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        # Quit button setup
        QUIT_BUTTON = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(300, 700),
                             text_input="離開", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, URL_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Play
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()

                # Options
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()

                # Url
                if URL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    url()

                # Exit
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
