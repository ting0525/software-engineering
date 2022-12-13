import pygame

from Utils.ImageLoader import ImageLoader
from Utils.Initializer import Initializer
from Utils.SoundLoader import SoundLoader
from Variable import Variable
from Codes.Objects.Rock import Rock
import requests

# var = Variable()
img = ImageLoader()
initer = Initializer()
sound = SoundLoader()


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(Variable.font_name, size)
    text_surface = font.render(text, True, Variable.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

def new_rock():
    r = Rock()
    Variable.all_sprites.add(r)
    Variable.rocks.add(r)

def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (hp/100)*BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, Variable.GREEN, fill_rect)
    pygame.draw.rect(surf, Variable.WHITE, outline_rect, 2)

def draw_lives(surf, lives, img, x, y):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 32*i
        img_rect.y = y
        surf.blit(img, img_rect)

'''
def draw_init():
    initer.screen.blit(img.background_img, (0,0))
    draw_text(initer.screen, '太空生存戰!', 64, var.WIDTH/2, var.HEIGHT/4)
    draw_text(initer.screen, '← →移動飛船 空白鍵發射子彈~', 22, var.WIDTH/2, var.HEIGHT/2)
    draw_text(initer.screen, '按任意鍵開始遊戲!', 18, var.WIDTH/2, var.HEIGHT*3/4)
    pygame.display.update()
    waiting = True
    while waiting:
        initer.clock.tick(var.FPS)
        # 取得輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYDOWN:
                waiting = False
                return False
'''
def frame():
    width1 = 500
    height1 = 600
    color_inactive = (100, 100, 200)
    color_active = (200, 200, 255)
    color = color_inactive
    text = ""
    active = False
    running = True

    screen = pygame.display.set_mode((width1, height1))
    
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
                        Variable.idtext = text
                        print(Variable.idtext)
                        running = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        text_surface = font.render(text, True, color)
        input_box_width = max(200, text_surface.get_width()+10)
        input_box.w = input_box_width
        input_box.center = (width1/2, height1/2)
    
        # 畫面更新
        screen.fill(Variable.BLACK)
        #screen.blit(background_img , (0,0))
        screen.blit(text_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 3)
        draw_text(screen , '輸入遊戲ID記錄你的分數' , 30 , 250 , 100)
        pygame.display.update()
        
        
        

def req_get(idtext , score , token):
    res = requests.get('http://localhost:80/api/add_message/1234', json={"id":idtext , "score":score , "my_token":token})
    if res.ok:
        print(res.json())