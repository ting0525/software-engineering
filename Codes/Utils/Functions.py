import sys

import pygame

from Utils.ImageLoader import ImageLoader
from Utils.Initializer import Initializer
from Utils.SoundLoader import SoundLoader
from Variable import Variable
from Objects.Rock import Rock
import requests

var = Variable()
img = ImageLoader()
initer = Initializer()
sound = SoundLoader()


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(Variable.FONT_NAME, size)
    text_surface = font.render(text, True, Variable.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


def new_rock():
    r = Rock()
    Variable.ALL_SPRITES.add(r)
    Variable.ROCKS.add(r)


def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 200
    BAR_HEIGHT = 20
    fill = (hp / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, Variable.GREEN, fill_rect)
    pygame.draw.rect(surf, Variable.WHITE, outline_rect, 2)


def draw_lives(surf, lives, img, x, y):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 32 * i
        img_rect.y = y
        surf.blit(img, img_rect)


def frame():
    color_inactive = (100, 100, 200)
    color_active = (200, 200, 255)
    color = color_inactive
    text = ""
    active = False
    running = True

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.update()
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(100, 100, 140, 50)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                active = True if input_box.collidepoint(event.pos) else False

                # 輸入框顏色設定
                color = color_active if active else color_inactive

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        Variable.IDTEXT = text
                        print(Variable.IDTEXT)
                        running = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        text_surface = font.render(text, True, color)
        input_box_width = max(200, text_surface.get_width() + 10)
        input_box.w = input_box_width
        input_box.center = (400 / 2, 400 / 2)

        # 畫面更新
        screen.fill(Variable.BLACK)
        screen.blit(img.currentBackground, (0, 0))

        # screen.blit(background_img , (0,0))
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 3)
        draw_text(screen, '輸入遊戲ID記錄你的分數', 30, 250, 100)
        pygame.display.update()


def req_get(idtext, score, token):
    res = requests.get('http://127.0.0.1:80/api/add_message/1234',
                       json={"id": idtext, "score": score, "my_token": token})
    if res.ok:
        print(res.json())
